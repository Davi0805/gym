# Generated by Django 5.0.3 on 2024-04-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_log_exerc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercparam',
            name='exerc',
            field=models.CharField(default='desconhecido', max_length=50),
        ),
    ]