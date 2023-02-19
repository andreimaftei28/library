# Generated by Django 4.1.7 on 2023-02-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='preview',
            field=models.FileField(null=True, upload_to='static/previews'),
        ),
    ]
