# Generated by Django 5.1.2 on 2024-11-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_created_at_employee_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='custom_fields',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
