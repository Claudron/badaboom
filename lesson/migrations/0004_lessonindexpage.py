# Generated by Django 4.1.3 on 2022-11-15 12:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
        ("lesson", "0003_lessonpage_delete_lessonindexpage"),
    ]

    operations = [
        migrations.CreateModel(
            name="LessonIndexPage",
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
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
    ]
