# Generated by Django 5.0.3 on 2024-04-04 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_exercset_exercname_exercset_exercname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protocolo01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercname', models.CharField(max_length=30)),
                ('exercset', models.IntegerField()),
                ('exercminrep', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Exercicios',
        ),
        migrations.RemoveField(
            model_name='protocolo1',
            name='exerc',
        ),
        migrations.DeleteModel(
            name='Exercset',
        ),
        migrations.DeleteModel(
            name='Protocolo1',
        ),
    ]
