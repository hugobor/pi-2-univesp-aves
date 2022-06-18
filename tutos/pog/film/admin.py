from django.contrib import admin

from .models import Filme, Genero
# Register your models here.
admin.site.register( Filme )
admin.site.register( Genero )
