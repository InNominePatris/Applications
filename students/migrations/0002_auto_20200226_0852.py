# Generated by Django 2.2 on 2020-02-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]