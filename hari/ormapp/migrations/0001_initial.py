# Generated by Django 5.0.3 on 2024-03-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_DB',
            fields=[
                ('b_id', models.IntegerField(primary_key='b_id', serialize=False)),
                ('b_name', models.CharField(max_length=100)),
                ('b_author', models.CharField(max_length=100)),
                ('b_edition', models.CharField(max_length=20)),
                ('b_year', models.DateField()),
            ],
        ),
    ]