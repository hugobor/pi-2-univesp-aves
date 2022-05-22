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


# Notas

Um site pode ter várias apps.

Model = Objeto ORM. Armazenado no banco de dados. manage.py



+ Criando o Model de posts para o blog.
+ Fazer `./migrations.py migrate` para atualizar o banco de dados
