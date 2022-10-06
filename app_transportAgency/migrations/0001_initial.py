# Generated by Django 3.2.3 on 2021-07-16 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_bus', models.CharField(max_length=50)),
                ('seatings', models.IntegerField(default=48)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.TextField()),
                ('destiny', models.TextField()),
                ('route_time', models.TimeField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_schedule', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_seating', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='TripScheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_trip', models.DateField(auto_now_add=True)),
                ('state', models.CharField(choices=[('2', 'en viaje'), ('4', 'cancelado'), ('1', 'A tiempo'), ('3', 'finalizado')], default='1', max_length=1)),
                ('routes', models.ManyToManyField(blank=True, null=True, to='app_transportAgency.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField()),
                ('ticket_quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('routes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transportAgency.route')),
                ('seating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_transportAgency.bus')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_transportAgency.schedule'),
        ),
        migrations.AddField(
            model_name='bus',
            name='name_seating',
            field=models.ManyToManyField(to='app_transportAgency.Seating'),
        ),
    ]
