# Generated by Django 4.0.5 on 2022-06-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aves', '0006_fotoave'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassifiExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reino', models.CharField(blank=True, max_length=2048, null=True)),
                ('filo', models.CharField(blank=True, max_length=2048, null=True)),
                ('classe', models.CharField(max_length=2048)),
            ],
            options={
                'verbose_name': 'classificação extra',
                'verbose_name_plural': 'classificações estras',
                'ordering': ['classe'],
            },
        ),
        migrations.AddField(
            model_name='ordem',
            name='classifiextra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aves.classifiextra', verbose_name='classificação extra'),
        ),
    ]
