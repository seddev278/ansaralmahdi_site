from django.urls import path
from .import views


urlpatterns = [
    path('aaza/',views.list_afrad,name='list_afrad')
]
