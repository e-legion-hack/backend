from django.db import migrations

from utils.enums import City, Department as EnumDepartament


def insert_employee_data(apps, schema_editor):
    Office = apps.get_model("office", "Office")
    Departament = apps.get_model('office', 'Departament')

    Office.objects.create(
        city=City.moscow.name,
        name='Главный',
        address='117246, Научный проезд 8 стр.1, офис 431',
        phone='84996537156',
        email='sales@dz.ru',
    )
    Office.objects.create(
        city=City.spb.name,
        name='второй',
        address='197374, ул. Оптиков 4',
        phone='88122009509',
        email='hello@e-legion.com',
    )
    Office.objects.create(
        city=City.kazan.name,
        name='третий',
        address='420107, ул. Петербургская 50, к. 5, офис 404',
        phone='88435705407',
        email='kazan@dz.ru',
    )
    Office.objects.create(
        city=City.ufa.name,
        name='четвертый',
        address='450076, ул. Чернышевского 82, к. 6, бизнес-центр Капитал, офис 615',
        phone='84996537156',
        email='ufa@dz.ru',
    )
    Office.objects.create(
        city=City.kalinin.name,
        name='западный',
        address='236022, ул. Карла Маркса 59',
        phone='78122009509',
        email='hello@e-legion.com',
    )

    for dep in EnumDepartament:
        Departament.objects.create(name=dep.name)


class Migration(migrations.Migration):
    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_employee_data)
    ]
