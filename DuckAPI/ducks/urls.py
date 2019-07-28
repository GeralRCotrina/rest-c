
from django.contrib import admin
from django.urls import path,re_path
from ducks.views import *

urlpatterns = [
    re_path(r'^ducks/$',DuckList.as_view(),name='ducks'),
]
