# Generated by Django 4.0.5 on 2022-06-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cientifico', models.CharField(max_length=2048, unique=True, verbose_name='nome científico')),
                ('nome_popular', models.CharField(blank=True, max_length=2048, null=True, verbose_name='nome popular')),
                ('nome_ingles', models.CharField(blank=True, max_length=2048, null=True, verbose_name='nome em inglês')),
                ('estado_iucn_sp', models.CharField(choices=[('LC', 'Pouco Preocupante'), ('NT', 'Quase Ameaçada'), ('VU', 'Vulnerável'), ('EN', 'Em Perigo'), ('CR', 'Criticamente em Perigo'), ('EW', 'Extinta na Natureza'), ('EX', 'Extinta'), ('DD', 'Dados Insuficientes'), ('NE', 'Não Avaliada')], max_length=2, null=True, verbose_name='estado de conservação em São Paulo')),
                ('descricao', models.TextField(blank=True)),
                ('imagem_capa', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
