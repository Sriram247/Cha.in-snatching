# Generated by Django 4.1.2 on 2022-10-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Photos',
            field=models.FileField(blank=True, upload_to='Photos'),
        ),
    ]
