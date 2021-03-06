from django.db import models, migrations


def load_data(apps, schema_editor):
    Flavor = apps.get_model("api", "Flavor")

    Flavor(
        name="Margarita"
    ).save()
    Flavor(
        name="Marinara"
    ).save()
    Flavor(
        name="Salami"
    ).save()
    Flavor(
        name="Pastrami"
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201112_1822'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
