from django.contrib import admin

from .models import Ave, Ordem, Familia, InfoExtra

# Register your models here.

class InfoExtraInline( admin.StackedInline ):
    model = InfoExtra

class AveAdmin( admin.ModelAdmin ):
    inlines = [ InfoExtraInline ]
    
admin.site.register( Ave, AveAdmin )
admin.site.register( Ordem )
admin.site.register( Familia )

