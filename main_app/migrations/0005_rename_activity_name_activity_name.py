# Generated by Django 4.2.4 on 2023-08-23 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_travelitinerary_end_date_alter_travelitinerary_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_name',
            new_name='name',
        ),
    ]