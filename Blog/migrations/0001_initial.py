# Generated by Django 4.1 on 2022-08-14 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 11, 17, 14, 69523, tzinfo=datetime.timezone.utc))),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2022, 8, 14, 11, 17, 14, 69523, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
