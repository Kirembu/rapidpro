# Generated by Django 2.2.20 on 2021-07-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0153_auto_20210712_1723"),
    ]

    operations = [
        migrations.AlterField(
            model_name="broadcastmsgcount",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="broadcastmsgcount",
            name="is_squashed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="labelcount",
            name="count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="labelcount",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="labelcount",
            name="is_archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="labelcount",
            name="is_squashed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="systemlabelcount",
            name="count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="systemlabelcount",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="systemlabelcount",
            name="is_archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="systemlabelcount",
            name="is_squashed",
            field=models.BooleanField(default=False),
        ),
    ]