from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from freeGEZ.settings import BASE_DIR

def base(request):
    if request.method == 'GET':
        return render(request, 'heritage_register/card_pattern.html', {})

class GeneratePdf(View):

    def get(self, request):
        rules=''
        with open('{}/static/heritage_register/style.css'.format(BASE_DIR)) as f2:
            rules = f2.read()
        html = HTML(filename='{}/templates/heritage_register/card_pattern.html'.format(BASE_DIR))
        font_conf = FontConfiguration()
        css = CSS(string=rules,  font_config=font_conf)
        pdf = html.write_pdf(stylesheets=[css], font_config=font_conf)
        return HttpResponse(pdf, content_type='application/pdf')

