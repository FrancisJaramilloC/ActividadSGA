# Generated by Django 5.0.6 on 2024-05-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallaCurricular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
                ('titulo', models.CharField(max_length=100)),
            ],
        ),
    ]
