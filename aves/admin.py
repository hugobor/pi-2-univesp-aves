from django.contrib import admin

from .models import Ave, Ordem, Familia, InfoExtra, FotoAve, ClassifiExtra

# Register your models here.

class InfoExtraInline( admin.StackedInline ):
    model = InfoExtra

class FotoAveInline( admin.StackedInline ):
    model = FotoAve

class AveAdmin( admin.ModelAdmin ):
    inlines = [ InfoExtraInline, FotoAveInline ]
    
admin.site.register( Ave, AveAdmin )


class FamiliaInline( admin.TabularInline ):
    model = Familia

class OrdemAdmin( admin.ModelAdmin ):
    inlines = [ FamiliaInline ]
    
admin.site.register( Ordem, OrdemAdmin )
admin.site.register( Familia )
admin.site.register( ClassifiExtra )

