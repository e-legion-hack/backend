# Generated by Django 3.2.7 on 2021-10-03 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedactivity',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tinder.activity'),
        ),
    ]
