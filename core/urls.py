from django.contrib import admin
from django.urls import path, include
from galeria.views import galeria

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('galeria', include('galeria.urls')), outra forma de fazer.
    path('', galeria), 
]
