# Generated by Django 3.0.4 on 2020-04-08 15:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200408_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useredudetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 15, 8, 7, 132138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 15, 8, 7, 131139, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userskilldetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 15, 8, 7, 133137, tzinfo=utc)),
        ),
    ]
