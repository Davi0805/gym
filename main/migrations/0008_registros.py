# Generated by Django 5.0.3 on 2024-04-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_protocolo02_protocolo03_protocolo04'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('peso1', models.IntegerField()),
                ('peso2', models.IntegerField()),
                ('peso3', models.IntegerField()),
                ('peso4', models.IntegerField()),
                ('peso5', models.IntegerField()),
                ('peso6', models.IntegerField()),
            ],
        ),
    ]
