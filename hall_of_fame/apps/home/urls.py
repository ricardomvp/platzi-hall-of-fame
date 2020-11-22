from django.urls import path

from apps.home.views import *

urlpatterns = [
    path('page/<str:page>', home, name='page'),
]
