# Generated by Django 4.0 on 2023-09-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0010_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='H5Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weights', models.FileField(upload_to='models/weights/')),
            ],
        ),
    ]
