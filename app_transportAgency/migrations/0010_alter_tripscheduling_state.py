# Generated by Django 3.2.3 on 2021-07-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transportAgency', '0009_alter_tripscheduling_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripscheduling',
            name='state',
            field=models.CharField(choices=[('2', 'en viaje'), ('4', 'cancelado'), ('3', 'finalizado'), ('1', 'A tiempo')], default='1', max_length=1),
        ),
    ]