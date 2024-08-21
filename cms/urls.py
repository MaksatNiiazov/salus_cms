from django.contrib import admin
from django.urls import path

from cms.views import SiteView

urlpatterns = [
    path('', SiteView.as_view(), name='index'),

]