# Generated by Django 3.0.4 on 2020-04-09 00:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200409_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useredudetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 0, 46, 46, 413922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 0, 46, 46, 412922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userskilldetails',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 0, 46, 46, 414921, tzinfo=utc)),
        ),
    ]