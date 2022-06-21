# Instalação

+ Usar virtualenv e pip para instalar pacotes
+ Django e psycopg2 no arquivo `requeriments.txt`
+ django-extensions para usar o runscript
+ `pip install -r requeriments.txt`
+ Precisa do python3-devel e libpq-devel para instalar o psycopg2
+ Lembrar de usar startapp e colocar os models no admin.py


# Generic Views

Template padrão é `<app_name>/<model_name>_<tipo_de_view>.html`, pode ser trocado com `template_name`.
Campo pk para primary key.
Variável de contexto tem o nome do model em caixa baixa. Pode ser trocado com `context_object_name`.
Para ListView a veriável é `<nome_modelo>_list`.


# Testes

`from django.test.util import setup_test_environmnent`
`from django.test import Client`
