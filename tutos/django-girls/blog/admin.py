from django.contrib import admin

# Register your models here.
# 👆 Fazer isso pra usar no django-admin

from .models import Post

admin.site.register( Post ) #!!!!

