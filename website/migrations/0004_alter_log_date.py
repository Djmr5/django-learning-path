# Generated by Django 4.1.7 on 2023-04-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alumno_alter_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(verbose_name='date added'),
        ),
    ]
