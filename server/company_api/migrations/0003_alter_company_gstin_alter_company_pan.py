# Generated by Django 4.1.7 on 2023-02-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company_api", "0002_rename_companyid_company_company_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="gstin",
            field=models.CharField(max_length=99, unique=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="pan",
            field=models.CharField(max_length=99, unique=True),
        ),
    ]