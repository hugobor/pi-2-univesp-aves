# Django Girls

```bash
$ virtualenv myvenv
$ source myvenv/bin/activate
$ pip install -U pip
```

+ arquivo requirements.txt

```bash
Django~=3.2.10
```

```
$ pip install -r requirements.text
```

```
$ django-admin startproject mysite .
```

* Arquivi setting.py

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
STATIC_ROOT = BASE_DIR / 'static'
```

```bash
$ ./manage.py migrate
$ ./manage.py runserver
```




```bash
$ ./manage.py startapp blog
```

Colocar app blog em ~INSTALLED_APPS~ em ~settings.py~.

+ Criar modelo...

```bash
$ ./manage.py makemigrations blog
$ ./manage.py migrate blog
```

+ Registrar modelo em admim.py

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Hora do `runserver`

http://127.0.0.1:8000/admin

Precisa de um superuser para acessar

```bash
$ ./manage.py createsuperuser
```

+ fazer login no site `/admin`

🤯 Aparece os coiso tudo

Dá pra ver os dados criados no arquivo db.sqlite3
Salva os registros de Post na tabela `blog_post`

Mágia impressionante 

+ Adicionar url em `urls.py` no site e no app.
+ Adicionar render do template no coiso da url do app

# QuerySet

Console Django:

```bash
$ ./manage.py shell
```

Mesma coisa do shell Python, mas com as coisas do Django junto...

```python
>>> from blog.models import Post
>>> Post.objects.all()
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> me = User.objects.get( username = 'hugo' )
>>> Post.objects.create( author = me, title = 'Biloba', text = "Somos todos felizes!" )
>>> 'etc etc etc'
>>> Post.objects.filter( author = me )
>>> Post.objects.filter( text__contains = 'amogus' )
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
>>> Post.objects.all().order_by( 'title' )
```


imprime variáveis com {{ }}

Arquivos estáticos na pasta `static`.

https://www.webfx.com/web-design/color-picker/

CSS selectors.

Para usar arquivos estáticos:

```
{% load static %}
```

No arquivo de template

Herança de templates funciona igual ao Jinja.

```
{% block blop %}
{% endblock %}

{% extends 'blup/blap' %} #pesquisa na pasta templates

{% block title %}Título porco{% endblock %}
```

Url nos templates
```
{% url 'blop_url' pk=post.pk %}
```

pk é o campo da chave primária dos models.

Use `get_object_or_404` para pegar modelos que podem não existir.
Parâmetros de url aparecem na função da view.

# Notas

Um site pode ter várias apps.

Model = Objeto ORM. Armazenado no banco de dados. manage.py



+ Criando o Model de posts para o blog.
+ Fazer `./migrations.py migrate` para atualizar o banco de dados
