# Generated by Django 4.1.3 on 2023-05-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inventory',
            field=models.BooleanField(default=True),
        ),
    ]
