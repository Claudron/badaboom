# Generated by Django 4.1.3 on 2022-11-17 13:40

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("lesson", "0009_lessoncategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="lessonpage",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="lesson.lessoncategory"
            ),
        ),
    ]