from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.views.generic import View, CreateView, DeleteView, DetailView, ListView, UpdateView
from django.template.loader import get_template

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from freeGEZ.settings import BASE_DIR

from .forms import CustomUserCreationForm
from .models import Relic
from suds.client import Client


# def base(request):
#     if request.method == 'GET':
#         return render(request, 'heritage_register/card_pattern.html', {})
def get_wsdl():
    client = Client('https://uslugaterytws1.stat.gov.pl/wsdl/terytws1.wsdl')
    HeaderMessage = client.factory.create('ns0:JednostkaPodzialuTerytorialnego')
    gmina = client.service.WyszukajJPT('Zabrodzie').GmiNazwa
    print(gmina)


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
    login_url = reverse_lazy('login')
    context_object_name = 'relic'
    fields = ['name', 'time_of_creation', 'image']
    model = Relic
    success_url = reverse_lazy('relic-details')  # TODO: change url to last updated page
    template_name = 'heritage_register/switch.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RelicUpdateView, self).get_context_data()
        context.update({'back_page': self.request.session['page']})
        return super().get_context_data(**context)


class CreateRelicView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    fields = '__all__'
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
        initial['province'] = 'mazowieckie'
        initial['district'] = 'wyszkowski'
        initial['municipality'] = 'Zabrodzie'
        initial['image'] = 'blank.png'
        return initial

    def get_context_data(self, **kwargs):
        context = super(CreateRelicView, self).get_context_data()
        if self.request.session.get('page'):
            context.update({'back_page': self.request.session['page']})
        return super().get_context_data(**context)


class GeneratePdf(View):

    def get(self, request, pk):
        # rules=''
        # with open('{}/static/heritage_register/style.css'.format(BASE_DIR)) as f2:
        #     rules = f2.read()
        # html = HTML(filename='{}/templates/heritage_register/card_pattern.html'.format(BASE_DIR))
        # font_conf = FontConfiguration()
        # css = CSS(string=rules,  font_config=font_conf)
        # pdf = html.write_pdf(stylesheets=[css], font_config=font_conf)
        # return HttpResponse(pdf, content_type='application/pdf')
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
