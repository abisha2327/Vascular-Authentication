# Generated by Django 4.0 on 2023-09-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='biometry',
            field=models.FileField(upload_to=''),
        ),
    ]
