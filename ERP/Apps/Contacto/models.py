from django.db import models

# Create your models here.

class Contacto(models.Model):
	TIPO_CONTACTO_CHOICE = (
		('Ind', 'Individual'),
		('Comp', 'Compañia'),
		)
	tipo_contacto_choice = models.CharField(max_length=255, choices=TIPO_CONTACTO_CHOICE, default='Ind')
	nombre = models.CharField(max_length=255)
	cedula = models.CharField(max_length=8, null=True, blank=True)
	TIPO_DIRECCION_CHOICE = (
		('con', 'Contacto'),
		('fact', 'Direccion de Factura'),
		('ent', 'Direccion de Entrega'),
		('otr', 'Otra Direccion'),
		('priv', 'Direccion Privada'),
		)
	tipo_direccion = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_DIRECCION_CHOICE)
	direccion = models.CharField(max_length=255, null=True, blank=True)
	rif = models.CharField(max_length=30, null=True, blank=True)
	puesto_trabajo = models.CharField(max_length=30, null=True, blank=True)
	telefono = models.CharField(max_length=8, null=True, blank=True)
	movil = models.CharField(max_length=8, null=True, blank=True)