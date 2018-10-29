from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from django.conf import settings
from easy_pdf.views import PDFTemplateView

def base(request):
    if request.method == 'GET':
        return render(request, 'heritage_register/card_pattern.html', {})

class GeneratePdf(PDFTemplateView):
    template_name = 'heritage_register/card_pattern.html'
    base_url = 'file://' + settings.STATICFILES_DIRS[0]
    download_filename = 'card.pdf'

    def get_context_data(self, **kwargs):
        return super(GeneratePdf, self).get_context_data(
            pagesize='A4',
            title='Address card',
            **kwargs
        )

