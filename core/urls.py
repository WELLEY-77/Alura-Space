from django.contrib import admin
from django.urls import path
from galeria.views import galeria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', galeria)
]
