# Generated by Django 5.0.3 on 2024-04-04 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_protocolo01_delete_exercicios_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protocolo02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercname', models.CharField(max_length=30)),
                ('exercset', models.IntegerField()),
                ('exercminrep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo03',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercname', models.CharField(max_length=30)),
                ('exercset', models.IntegerField()),
                ('exercminrep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo04',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercname', models.CharField(max_length=30)),
                ('exercset', models.IntegerField()),
                ('exercminrep', models.IntegerField()),
            ],
        ),
    ]
