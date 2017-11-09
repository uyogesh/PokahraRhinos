from django.conf.urls import url
from django.contrib import admin
from .views import IndexPage

urlpatterns = [
    url(r'^$',IndexPage.as_view(),name='IndexPage'),

]
