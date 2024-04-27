from django.db import models

# Create your models here.

class adltest(models.Model):
    id = models.AutoField(primary_key=True)
    campo1 = models.CharField(max_length=100)
    valor1 = models.IntegerField(default=0)  # Valor predeterminado de 0
