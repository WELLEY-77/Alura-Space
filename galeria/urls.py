from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria, name='home'),
    path('image/<int:foto_id>', views.image, name='image'),
]