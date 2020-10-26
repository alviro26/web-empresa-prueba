# Generated by Django 3.1.2 on 2020-10-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='media')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
        ),
    ]
