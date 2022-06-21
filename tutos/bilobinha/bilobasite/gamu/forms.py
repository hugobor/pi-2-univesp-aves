from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Game, Console, ScreenShot, DescricaoExtra

DescricaoFormSet = inlineformset_factory( Game,
                                          DescricaoExtra,
                                          fields = '__all__',
                                          extra = 3 )

ScreenShotFormSet = inlineformset_factory( Game,
                                           ScreenShot,
                                           fields = '__all__',
                                           extra = 4 )

