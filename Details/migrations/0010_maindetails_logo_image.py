# Generated by Django 5.0.4 on 2024-06-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0009_alter_maindetails_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindetails',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='logo_image/'),
        ),
    ]