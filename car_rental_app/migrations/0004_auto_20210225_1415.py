# Generated by Django 3.1.6 on 2021-02-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental_app', '0003_auto_20210216_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_millage',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='millage_done',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_millage',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
