from django.urls import path
from . import views

urlpatterns = [
    path('', views.galeria, name='home'),
    path('image/<int:foto_id>', views.image, name='image'),
    path('buscar/', views.buscar, name='buscar'),
    path('nova-imagem', views.nova_imagem, name='nova_imagem'),
    path('editar-imagem', views.editar_imagem, name='editar_imagem'),
    path('deletar-imagem', views.deletar_imagem, name='deletar_imagem'),
]