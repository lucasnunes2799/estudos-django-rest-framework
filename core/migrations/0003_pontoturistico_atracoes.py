# Generated by Django 3.2.9 on 2021-11-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '__first__'),
        ('core', '0002_alter_pontoturistico_aprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
