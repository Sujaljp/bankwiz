# Generated by Django 4.1.7 on 2023-02-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account_api", "0004_rename_bank_account_bank_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="account_number",
            field=models.CharField(max_length=99, unique=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="branch_code",
            field=models.CharField(max_length=99),
        ),
    ]
