# Generated by Django 3.2.9 on 2021-12-17 18:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=30, verbose_name='autor')),
                ('texto', ckeditor.fields.RichTextField(verbose_name='Comentario')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('aprobado', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.post')),
            ],
        ),
    ]