# Generated by Django 2.1.7 on 2019-08-09 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("djangopsi", "0003_auto_20190729_1445")]

    operations = [
        migrations.AddField(
            model_name="reportgroup",
            name="environment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="report_groups",
                to="djangopsi.Environment",
            ),
        )
    ]
