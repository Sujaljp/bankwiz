# Generated by Django 4.1.7 on 2023-02-25 20:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("transaction_api", "0003_rename_account_id_transaction_account_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="account",
            new_name="account_id",
        ),
        migrations.RenameField(
            model_name="transaction",
            old_name="bank",
            new_name="bank_id",
        ),
        migrations.RenameField(
            model_name="transaction",
            old_name="company",
            new_name="company_id",
        ),
        migrations.RenameField(
            model_name="transaction",
            old_name="user",
            new_name="user_id",
        ),
    ]
