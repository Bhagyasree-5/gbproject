# Generated by Django 5.0.6 on 2024-06-20 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0013_rename_chemical_name_chemicals_chem_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chemicals',
            name='Balance',
        ),
    ]
