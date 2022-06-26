# Generated by Django 4.0.5 on 2022-06-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aves', '0002_ordem_alter_ave_options_ave_abundancia_relativa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ave',
            name='descricao',
        ),
        migrations.AddField(
            model_name='ave',
            name='estado_iucn_int',
            field=models.CharField(choices=[('LC', 'Pouco Preocupante'), ('NT', 'Quase Ameaçada'), ('VU', 'Vulnerável'), ('EN', 'Em Perigo'), ('CR', 'Criticamente em Perigo'), ('EW', 'Extinta na Natureza'), ('EX', 'Extinta'), ('DD', 'Dados Insuficientes'), ('NE', 'Não Avaliada')], max_length=2, null=True, verbose_name='estado de conservação Internacional'),
        ),
        migrations.AddField(
            model_name='ave',
            name='info',
            field=models.TextField(blank=True, verbose_name='informações gerais'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='abundancia_relativa',
            field=models.IntegerField(null=True, verbose_name='abundância relativa'),
        ),
        migrations.AlterField(
            model_name='ave',
            name='imagem_capa',
            field=models.ImageField(null=True, upload_to='', verbose_name='imagem de capa'),
        ),
    ]