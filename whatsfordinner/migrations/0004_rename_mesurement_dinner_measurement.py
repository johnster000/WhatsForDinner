# Generated by Django 4.0.3 on 2022-03-21 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatsfordinner', '0003_rename_details_dinner_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dinner',
            old_name='mesurement',
            new_name='measurement',
        ),
    ]
