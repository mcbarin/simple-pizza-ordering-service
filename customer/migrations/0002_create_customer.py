from django.db import models, migrations


def load_data(apps, schema_editor):
    Customer = apps.get_model("customer", "Customer")

    Customer(
        name="Mehmet Cagatay",
        surname="Barin"
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
