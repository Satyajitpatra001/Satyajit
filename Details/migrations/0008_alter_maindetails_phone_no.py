# Generated by Django 5.0.4 on 2024-06-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0007_maindetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindetails',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
    ]