# Generated by Django 4.2.1 on 2023-05-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discrition',
            field=models.TextField(),
        ),
    ]
