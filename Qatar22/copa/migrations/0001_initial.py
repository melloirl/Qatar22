# Generated by Django 4.1.1 on 2022-09-13 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selecao',
            fields=[
                ('cod_selecao', models.IntegerField(db_column='Cod_Selecao', primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='Nome', max_length=45)),
                ('confederacao', models.CharField(db_column='Confederacao', max_length=45)),
                ('titulo', models.IntegerField(db_column='Titulo')),
                ('ranking', models.CharField(db_column='Ranking', max_length=45)),
            ],
            options={
                'db_table': 'selecao',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Alojamento',
            fields=[
                ('cod_alojamento', models.IntegerField(db_column='Cod_Alojamento', primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='Nome', max_length=45)),
                ('cidade', models.CharField(blank=True, db_column='Cidade', max_length=45, null=True)),
                ('bairro', models.CharField(blank=True, db_column='Bairro', max_length=45, null=True)),
                ('rua', models.CharField(blank=True, db_column='Rua', max_length=45, null=True)),
                ('cep', models.CharField(blank=True, db_column='CEP', max_length=45, null=True)),
                ('entrada', models.CharField(db_column='Entrada', max_length=45)),
                ('saida', models.CharField(db_column='Saida', max_length=45)),
                ('selecao_cod_selecao', models.ForeignKey(db_column='SELECAO_Cod_Selecao', on_delete=django.db.models.deletion.DO_NOTHING, to='copa.selecao')),
            ],
            options={
                'db_table': 'alojamento',
                'managed': True,
                'unique_together': {('cod_alojamento', 'selecao_cod_selecao')},
            },
        ),
    ]
