from django.db import models

class tinta (models.Model):
    id_tintas = models.AutoField(primary_key = True)
    marca = models.TextField(max_length = 255)
    modelo = models.TextField(max_length = 255)
    ano = models.IntegerField()
    codigo = models.TextField( max_length = 255)
    cor = models.TextField( max_length = 255)
    
