# Generated by Django 2.0.13 on 2020-06-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20200620_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='img/'),
        ),
    ]
