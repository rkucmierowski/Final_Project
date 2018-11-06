"""freeGEZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

from .settings import MEDIA_URL, MEDIA_ROOT
from heritage_register.views import CreateRelic, GeneratePdf, RelicDeleteView, RelicDetailsView, RelicsListView, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='heritage_register/card_pattern.html'), name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup/', SignUp.as_view(), name='signup'),
    path('pdf/', GeneratePdf.as_view()),
    path('relic/', CreateRelic.as_view(), name='relic'),
    re_path(r'^relics/$', RelicsListView.as_view(), name='relics-list'),
    re_path(r'^relic/(?P<pk>(\d)+)/$', RelicDetailsView.as_view(), name='relic-details'),
    re_path(r'^relic/(?P<pk>(\d)+)/delete/$', RelicDeleteView.as_view(), name='relic-delete'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
