# Generated by Django 4.1.3 on 2022-11-17 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
        ("lesson", "0006_lessonpagetag_lessonpage_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="LessonTagIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
    ]
