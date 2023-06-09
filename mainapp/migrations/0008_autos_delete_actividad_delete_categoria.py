# Generated by Django 4.2 on 2023-05-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0007_alter_actividad_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=500, verbose_name="Nombre")),
                ("marca", models.CharField(max_length=500, verbose_name="Marca")),
                ("modelo", models.IntegerField()),
                ("precio", models.FloatField()),
            ],
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias",},
        ),
        migrations.DeleteModel(name="Actividad",),
        migrations.DeleteModel(name="Categoria",),
    ]
