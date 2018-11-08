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
from heritage_register.views import CreateRelicView, GeneratePdf, RelicAllView, RelicDeleteView, RelicDetailsView, RelicsListView, RelicUpdateView, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='heritage_register/card_pattern.html'), name='home'),
    path('', RelicsListView.as_view(), name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup/', SignUp.as_view(), name='signup'),
    re_path(r'^pdf/(?P<pk>(\d)+)*$', GeneratePdf.as_view(), name='pdf'),
    re_path(r'^relic/$', CreateRelicView.as_view(), name='relic-create'),
    re_path(r'^relics/$', RelicsListView.as_view(), name='relics-list'),
    re_path(r'^relic/all/$', RelicAllView.as_view(), name='relic-all'),
    re_path(r'^relic/details/$', RelicDetailsView.as_view(), name='relic-details'),
    re_path(r'^relic/delete/(?P<pk>(\d)+)/$', RelicDeleteView.as_view(), name='relic-delete'),
    re_path(r'^relic/update/(?P<pk>(\d)+)/$', RelicUpdateView.as_view(), name='relic-update'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
