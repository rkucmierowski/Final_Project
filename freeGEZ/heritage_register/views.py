from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DeleteView, DetailView, ListView
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
    template_name = 'heritage_register/relics_list.html'
    queryset = Relic.objects.all()


class RelicDetailsView(DetailView):
    model = Relic
    template_name = 'heritage_register/relic_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next = Relic.objects.filter(pk=self.object.pk + 1)
        prev = Relic.objects.filter(pk=self.object.pk - 1)
        if next:
            context['next'] = next[0].pk
        if prev:
            context['prev'] = prev[0].pk
        return context


class RelicDeleteView(DeleteView):
    model = Relic
    success_url = reverse_lazy('home')


class CreateRelic(CreateView):
    model = Relic
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.data)
        return super(CreateRelic, self).form_valid(form)

    # def form_invalid(self, form):
    #     return HttpResponse("OO")


class GeneratePdf(View):

    def get(self, request):
        # rules=''
        # with open('{}/static/heritage_register/style.css'.format(BASE_DIR)) as f2:
        #     rules = f2.read()
        # html = HTML(filename='{}/templates/heritage_register/card_pattern.html'.format(BASE_DIR))
        # font_conf = FontConfiguration()
        # css = CSS(string=rules,  font_config=font_conf)
        # pdf = html.write_pdf(stylesheets=[css], font_config=font_conf)
        # return HttpResponse(pdf, content_type='application/pdf')

        html = HTML(url='http://localhost:8000/')
        pdf = html.write_pdf()
        return HttpResponse(pdf, content_type='application/pdf')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
