from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria),
    path('image/', views.image, name='image'),
]