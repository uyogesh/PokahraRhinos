from django.conf.urls import url
from django.contrib import admin
from .views import RegForm,Submit_form

urlpatterns = [
    # url(r'^$',RegForm.as_view(),name='RegistrationForm'),
    url(r'^',Submit_form),
]
