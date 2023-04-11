# Generated by Django 4.1.7 on 2023-04-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_log_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateTimeField(verbose_name='date added'),
        ),
    ]
