# Generated by Django 5.0.3 on 2024-04-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercset', models.IntegerField()),
                ('exercep', models.IntegerField()),
                ('exercname', models.ManyToManyField(to='main.exercicios')),
            ],
        ),
    ]
