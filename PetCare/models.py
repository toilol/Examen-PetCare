from django.db import models

# Create your models here.
class Servicio(models.Model):
        id_servicio = models.AutoField(db_column='idServicio', primary_key=True)
        precio = models.CharField(max_length=10, null=True, default=None)
        imagen = models.ImageField(upload_to='servicio/', null='media/default.png')
        descripcion = models.TextField()