from django.contrib import admin

from gamu.models import DescricaoExtra, ScreenShot, Game, Console

# Register your models here.
class DescricaoInlineAdmin( admin.StackedInline ):
    model = DescricaoExtra

class ScreenShotInlineAdmin( admin.TabularInline ):
    model = ScreenShot


class GameAdmin( admin.ModelAdmin ):
    model = Game
    inlines = [
        DescricaoInlineAdmin,
        ScreenShotInlineAdmin,
    ]


admin.site.register( Game, GameAdmin )
admin.site.register( Console )

