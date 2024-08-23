from django.contrib import admin
from django.urls import path

from cms.views import SiteView, CreateRequestView

urlpatterns = [
    path('', SiteView.as_view(), name='index'),
    path('request/', CreateRequestView.as_view(), name='request'),

]