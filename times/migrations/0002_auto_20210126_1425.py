# Generated by Django 3.1.5 on 2021-01-26 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserved',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='times.service'),
        ),
    ]
