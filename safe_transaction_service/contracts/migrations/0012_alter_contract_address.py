# Generated by Django 5.0.7 on 2024-07-19 12:53

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0011_alter_contract_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="address",
            field=gnosis.eth.django.models.EthereumAddressBinaryField(
                primary_key=True, serialize=False
            ),
        ),
    ]