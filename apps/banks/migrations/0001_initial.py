# Generated by Django 5.1.4 on 2025-01-15 12:02


from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("branch", models.CharField(max_length=100)),
                ("is_islamic", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
