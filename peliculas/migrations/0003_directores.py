# Generated by Django 4.1.4 on 2023-01-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_remove_peliculas_fecha_de_lanzamiento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo')], max_length=10)),
            ],
        ),
    ]
