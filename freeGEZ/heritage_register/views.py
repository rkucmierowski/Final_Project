import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf

def base(request):
    if request.method == 'GET':
        return render(request, 'heritage_register/card_pattern.html', {})

class GeneratePdf(View):
    def get(self, request):
        pdf = render_to_pdf('heritage_register/card_pattern.html',{})
        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not not not")
