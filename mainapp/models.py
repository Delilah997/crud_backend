from django.db import models

# Create your models here.

class Autos(models.Model):
    """Model definition for Autos."""
    nombre = models.CharField('Nombre',max_length=500)
    marca = models.CharField('Marca',max_length=500)
    modelo = models.IntegerField()
    precio = models.FloatField()


    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):

        return self.nombre
