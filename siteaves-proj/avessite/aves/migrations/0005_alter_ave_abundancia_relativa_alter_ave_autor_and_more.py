# Generated by Django 4.0.5 on 2022-06-24 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aves', '0004_alter_familia_options_alter_ordem_options_infoextra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ave',
            name='abundancia_relativa',
            field=models.IntegerField(blank=True, null=True, verbose_name='abundância relativa'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='autor',
            field=models.CharField(blank=True, max_length=2048, null=True, verbose_name='nome do autor'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='estado_iucn_int',
            field=models.CharField(blank=True, choices=[('LC', 'Pouco Preocupante'), ('NT', 'Quase Ameaçada'), ('VU', 'Vulnerável'), ('EN', 'Em Perigo'), ('CR', 'Criticamente em Perigo'), ('EW', 'Extinta na Natureza'), ('EX', 'Extinta'), ('DD', 'Dados Insuficientes'), ('NE', 'Não Avaliada')], max_length=2, null=True, verbose_name='estado de conservação Internacional'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='estado_iucn_sp',
            field=models.CharField(blank=True, choices=[('LC', 'Pouco Preocupante'), ('NT', 'Quase Ameaçada'), ('VU', 'Vulnerável'), ('EN', 'Em Perigo'), ('CR', 'Criticamente em Perigo'), ('EW', 'Extinta na Natureza'), ('EX', 'Extinta'), ('DD', 'Dados Insuficientes'), ('NE', 'Não Avaliada')], max_length=2, null=True, verbose_name='estado de conservação em São Paulo'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='familia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aves.familia', verbose_name='família'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='frequencia_ocorrencia',
            field=models.IntegerField(blank=True, null=True, verbose_name='frequência de ocorrência'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='imagem_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagem de capa'),
        ),
    ]
