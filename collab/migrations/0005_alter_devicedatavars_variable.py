# Generated by Django 4.2.6 on 2023-10-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0004_devicedatavars_remove_devicedata_decodedpayload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicedatavars',
            name='variable',
            field=models.CharField(max_length=250),
        ),
    ]
