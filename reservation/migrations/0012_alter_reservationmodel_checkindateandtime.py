# Generated by Django 4.2.9 on 2024-04-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_alter_reservationmodel_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='checkInDateandTime',
            field=models.DateField(auto_now_add=True),
        ),
    ]
