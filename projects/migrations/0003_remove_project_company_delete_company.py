# Generated by Django 5.1.2 on 2024-11-07 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_company_project_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="company",
        ),
        migrations.DeleteModel(
            name="Company",
        ),
    ]
