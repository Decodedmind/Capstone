# Generated by Django 4.1.5 on 2023-07-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItem",
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
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Appetizer", "Appetizer"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                            ("Dessert", "Dessert"),
                            ("Wine", "Wine"),
                        ],
                        max_length=50,
                    ),
                ),
                ("description", models.TextField(blank=True, max_length=200)),
                ("price", models.FloatField()),
                ("current", models.IntegerField(default=1)),
            ],
        ),
    ]
