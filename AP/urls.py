from django.urls import path

from . import views 


urlpatterns = [
    path('userdetails/', views.show, name='showy')
]

