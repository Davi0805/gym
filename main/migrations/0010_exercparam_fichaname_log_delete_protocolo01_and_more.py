# Generated by Django 5.0.3 on 2024-04-05 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_registros_ficha_alter_registros_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercparam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('serie', models.IntegerField(default=3, null=True)),
                ('repetmin', models.IntegerField(blank=True, default=10, null=True)),
                ('repetmax', models.IntegerField(blank=True, default=12, null=True)),
                ('pesomin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fichaname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('peso', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Protocolo01',
        ),
        migrations.DeleteModel(
            name='Protocolo02',
        ),
        migrations.DeleteModel(
            name='Protocolo03',
        ),
        migrations.DeleteModel(
            name='Protocolo04',
        ),
        migrations.DeleteModel(
            name='Registros',
        ),
        migrations.AddField(
            model_name='exercparam',
            name='ficha',
            field=models.ManyToManyField(to='main.fichaname'),
        ),
        migrations.AddField(
            model_name='log',
            name='exerc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exercparam'),
        ),
    ]