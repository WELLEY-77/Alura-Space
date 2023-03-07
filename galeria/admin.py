from django.contrib import admin
from .models import Fotografia

class ListaFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_per_page = 10

admin.site.register(Fotografia, ListaFotografias)
