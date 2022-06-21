# Generated by Django 4.0.5 on 2022-06-20 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=2048)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=2048)),
                ('imagem_capa', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem de Capa')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('ano', models.PositiveIntegerField(verbose_name='ano de lançamento')),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamu.console')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
