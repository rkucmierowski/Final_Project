from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DeleteView, ListView, UpdateView
from datetime import datetime

from weasyprint import HTML
from zeep import Client
from zeep.wsse.username import UsernameToken

from .forms import CustomUserCreationForm
from .models import Relic


def get_jpt(teryt):
    client = Client("https://uslugaterytws1test.stat.gov.pl/wsdl/terytws1.wsdl",
                    wsse=UsernameToken(username='TestPubliczny', password='1234abcd'))
    client.create_service(binding_name='{http://tempuri.org/}custom',
                          address='https://uslugaterytws1test.stat.gov.pl/terytws1.svc')
    if client.service.CzyZalogowany() == True:
        factory = client.type_factory('ns2')
        identyfiks = factory.identyfikatory(terc=teryt)
        list_identyfiks = factory.ArrayOfidentyfikatory(identyfiks)
        jpt = client.service.WyszukajJednostkeWRejestrze(identyfiks=list_identyfiks, kategoria='3',
                                                         DataStanu=datetime.now())
        if jpt != None:
            jpt = jpt[0]
            result = {i: jpt[i] for i in jpt if i == 'GmiNazwa' or i == 'Powiat' or i == 'Wojewodztwo'}
            return result
    else:
        return None


class RelicsListView(ListView):
    queryset = Relic.objects.all().order_by('pk')

    def get(self, request, *args, **kwargs):
        if request.session.get('page'):
            print(request.session.get('page'))
            del request.session['page']
        return super().get(request)


class RelicDetailsView(ListView):
    context_object_name = 'relics_list'
    model = Relic
    paginate_by = 1
    queryset = Relic.objects.all().order_by('pk')
    template_name = 'heritage_register/switch.html'

    def get(self, request, *args, **kwargs):
        super(RelicDetailsView, self).get(self, request, *args, **kwargs)
        context = self.get_context_data()
        request.session['page'] = str(context['page_obj'].number)
        return self.render_to_response(context)


class RelicAllView(ListView):
    context_object_name = 'relics_list'
    model = Relic
    queryset = Relic.objects.all().order_by('pk')
    template_name = 'heritage_register/switch.html'


class RelicDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Relic
    success_url = reverse_lazy('relics-list')


class RelicUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'relic'
    fields = ['name',
              'time_of_creation',
              'place',
              'address',
              'province',
              'district',
              'municipality',
              'forms_of_protection',
              'image',
              'description'
              ]
    login_url = reverse_lazy('login')
    model = Relic
    success_url = reverse_lazy('relic-details')  # TODO: change url to last updated page
    template_name = 'heritage_register/switch.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RelicUpdateView, self).get_context_data()
        context.update({'back_page': self.request.session['page']})
        return super().get_context_data(**context)


class CreateRelicView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    login_url = reverse_lazy('login')
    model = Relic
    success_url = reverse_lazy('relics-list')
    template_name = 'heritage_register/switch.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            form.image = self.request.FILES['image'].name
        except:
            form.image = 'blank.png'
        return super(CreateRelicView, self).form_valid(form)

    def get_initial(self):
        initial = super(CreateRelicView, self).get_initial()
        teryt = str(self.request.user.teryt)
        jpt = get_jpt(teryt=teryt)
        if jpt != None:
            initial['province'] = jpt['Wojewodztwo']
            initial['district'] = jpt['Powiat']
            initial['municipality'] = jpt['GmiNazwa']
        initial['image'] = 'blank.png'
        return initial

    def get_context_data(self, **kwargs):
        context = super(CreateRelicView, self).get_context_data()
        if self.request.session.get('page'):
            context.update({'back_page': self.request.session['page']})
        return super().get_context_data(**context)


class GeneratePdf(View):

    def get(self, request, pk):
        url = '{}://{}/relic'.format(request.scheme, request.get_host())
        if pk:
            url += '/details/?page={}'.format(pk)
        else:
            url += '/all'

        html = HTML(url=url)
        pdf = html.write_pdf()
        return HttpResponse(pdf, content_type='application/pdf')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
