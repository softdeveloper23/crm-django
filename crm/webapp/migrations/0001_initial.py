# Generated by Django 5.0.1 on 2024-01-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email_address", models.EmailField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("province", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=10)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
    ]
