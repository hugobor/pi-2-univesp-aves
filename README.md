# pi-2-univesp-aves
Projeto Integrador II - Univesp - Polo Santo André - Grupo 102

Continuidade de https://github.com/hugobor/projeto-integrador-aves

[Relatório Parcial](https://docs.google.com/document/d/1M4Nki4ytIAsv0m_NU1hezAc1a96qPrabzQhn2Iyu0ew/edit?usp=sharing)

# Para iniciar

```bash
$ virtualenv myvenv
$ source myvenv/bin/activate
$ pip install -r requirements.txt
$ ./manage.py makemigrations blog
$ ./manage.py migrate blog
$ ./manage.py migrate
$ ./manage.py runserver
```

Abrir http://localhost:8000 no navegador.

Acho que é isso...

# Projeto de Registro de Aves no Parque

+ Adicionar aqui as coisas do projeto do primeiro semestre
+ Lendo o tutorial do Django Girls. Vou adicionar aqui depois com notas.
+ Fazer o tutorial do sistema de votação do site oficial do Django depois
+ Tenho que colocar os coisos no relatório parcial

# Bibliografia/Tutoriais

## Django
+ [Django Girls](https://tutorial.djangogirls.org/en/)
+ [Django vs Flask](https://testdriven.io/blog/django-vs-flask/)
  +  Ver esse coiso. Pode ser usado como justificativa no relatório
+ [Referência para tipos em Models](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)
+ [Tipos no Django 4](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types)
+ [Django Admin](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)
+ [Views](https://docs.djangoproject.com/en/4.0/topics/http/views/)
+ [Arquivos estáticos](https://docs.djangoproject.com/en/4.0/howto/static-files/)
+ [Django com Bootstrap](https://dev.to/thalesbruno/django-projeto-generico-com-bootstrap-3d86)
+ [QuerySets](https://docs.djangoproject.com/en/4.0/ref/models/querysets/)
+ [Crud com class based views](https://towardsdatascience.com/build-a-django-crud-app-by-using-class-based-views-12bc69d36ab6)
+ [Deloy de Aplicativo em Django e PostgreSql no Azure](https://docs.microsoft.com/pt-br/azure/app-service/tutorial-python-postgresql-app?tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cazure-portal-access%2Cvscode-aztools-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions--zip-azcli%2Cdeploy-instructions-curl-bash)
+ [Hospedar arquivos de mídia no Azure](https://davidsantiago.fr/django-using-azure-blob-storage-to-handle-static-media-assets-from-scratch/)
+ [Arquivos .env](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)


## Postgres
+ [Postgres no Fedora](https://developer.fedoraproject.org/tech/database/postgresql/about.html)
+ [Documentação do Postgres](https://www.postgresql.org/docs/current/index.html)
+ [Tutorial Oficial](https://www.postgresql.org/docs/current/tutorial.html)
+ [Mais tutoriais](https://www.postgresqltutorial.com/)


## Outros
+ [Human Centered Design](https://drive.google.com/file/d/1tn2pg6GBNODpE4K-iL70vJPG_gS6eeof/preview)
+ [Tutorial da Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-20-04)
+ [Autenticação git](https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to)
+ [Lista de Fuso Horários](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)



# Coisas

+ Django
+ Heroku
+ PostgreSQL
+ Jinja
+ Django ORM
+ Bootstrap
+ etc... etc.. etc...
+ [Escolher cores](https://www.webfx.com/web-design/color-picker/)
+ [Google Fonts](https://fonts.google.com/) (para escolher fontes)

Tinha uma api de mapas livre que podia usar no lugar de pagar pelo Google Maps.
Dava para usar ela para colocar o lugar de onde foi tirada a foto dos pássaro.
Isso ia cumprir o requisito de usar api e núvem.
Ver sobre ela dispois

# Arrumar

+ Adicionar os documentos na pasta
+ Adicionar os outros membros do grupo no repositório
+ Usuários
  + Administrador: remove aves e coisos
  + Colaborador: manda fotos do pássiro
  + Anônimo: alopra tudo (?)
+ Cadastro de aves
+ Taxonomia das aves 
+ Cadastro de árvores (?)
+ Árveres que os bixo comi
