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
    queryset = Relic.objects.all()


class RelicDetailsView(ListView):
    model = Relic
    template_name = 'heritage_register/relic_details.html'
    context_object_name = 'relics_list'
    paginate_by = 1
    queryset = Relic.objects.all()


class RelicDeleteView(DeleteView):
    model = Relic
    success_url = reverse_lazy('relics-list')


class RelicUpdateView(UpdateView):
    fields = ['name','time_of_creation']
    model = Relic
    template_name = 'heritage_register/relic_update.html'
    success_url = reverse_lazy('relic-details')  #TODO: change url to last updated page


class CreateRelicView(CreateView):
    model = Relic
    fields = '__all__'
    success_url = reverse_lazy('relics-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.data)
        return super(CreateRelicView, self).form_valid(form)

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
