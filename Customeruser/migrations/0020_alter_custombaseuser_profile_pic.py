# Generated by Django 4.2.9 on 2024-04-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customeruser', '0019_alter_custombaseuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custombaseuser',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
