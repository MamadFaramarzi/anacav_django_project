# Generated by Django 5.0.7 on 2024-07-13 08:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[\\w\\d]+$')])),
                ('code', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(unique=True)),
                ('month', models.IntegerField(unique=True)),
                ('in_process', models.IntegerField(blank=True, null=True)),
                ('condition1', models.IntegerField(blank=True, null=True)),
                ('condition2', models.IntegerField(blank=True, null=True)),
                ('Condition3', models.IntegerField(blank=True, null=True)),
                ('total_condition', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
