# Generated by Django 3.0.3 on 2020-04-01 17:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=32)),
                ('district', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dr_name', models.CharField(max_length=128, null=True)),
                ('email_id_1', models.EmailField(max_length=128, null=True)),
                ('email_id_2', models.EmailField(max_length=128, null=True)),
                ('phone_1', models.EmailField(max_length=128, null=True)),
                ('phone_2', models.EmailField(max_length=128, null=True)),
                ('extension', models.EmailField(max_length=128, null=True)),
                ('source_link', models.EmailField(max_length=128, null=True)),
                ('source', models.EmailField(max_length=128, null=True)),
                ('details', models.EmailField(max_length=1024, null=True)),
                ('added_on', models.DateTimeField(default=datetime.datetime(2020, 4, 1, 17, 7, 18, 884322))),
                ('infotype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='data.InfoType')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='data.Location')),
            ],
        ),
    ]