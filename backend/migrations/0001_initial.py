# Generated by Django 4.1.2 on 2022-10-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='VideoFootages')),
                ('Photos', models.FileField(upload_to='Photos')),
            ],
        ),
    ]
