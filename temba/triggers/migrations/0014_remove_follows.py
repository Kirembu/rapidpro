# Generated by Django 2.0.8 on 2018-08-28 21:30

from django.db import migrations


def remove_follow_triggers(apps, schema_editor):
    Trigger = apps.get_model("triggers", "Trigger")

    triggers = Trigger.objects.filter(trigger_type="F", is_active=True)
    for trigger in triggers:
        trigger.is_active = False
        trigger.save(update_fields=("is_active",))
        print(f"Deactivated follow trigger #{trigger.id}")


class Migration(migrations.Migration):

    dependencies = [("triggers", "0013_auto_20180828_1955")]

    operations = [migrations.RunPython(remove_follow_triggers)]