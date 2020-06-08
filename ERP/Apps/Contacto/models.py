from django.db import models

# Create your models here.
TIPO_CONTACTO_CHOICE = (
		('Ind', 'Individual'),
		('Comp', 'Compañia'),
		)
TIPO_DIRECCION_CHOICE = (
		('con', 'Contacto'),
		('fact', 'Direccion de Factura'),
		('ent', 'Direccion de Entrega'),
		('otr', 'Otra Direccion'),
		('priv', 'Direccion Privada'),
		)

class Sector(models.Model):
	nombre = models.CharField(max_length=40)
	nombre_completo = models.CharField(max_length=255, null=True, blank=True)
	activo = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Sector"
		verbose_name_plural = "Sectores"
	def __str__(self):
		return self.nombre

class Compania(models.Model):
	#tipo_contacto_choice = models.CharField(max_length=255, choices=TIPO_CONTACTO_CHOICE, default='Ind')
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255, null=True, blank=True)
	rif = models.CharField(max_length=30, null=True, blank=True)
	telefono = models.CharField(max_length=8, null=True, blank=True)
	movil = models.CharField(max_length=8, null=True, blank=True)
	correo = models.EmailField(null=True, blank=True)
	pagina = models.URLField(null=True, blank=True)
	foto = models.ImageField(upload_to='fotos/contacto/', null=True, blank=True)
	sector = models.ForeignKey(Sector, null=True, blank=True, on_delete=models.SET_NULL)
	nota_interna = models.TextField(null=True, blank=True)
	class Meta:
		verbose_name = "Compañia"
		verbose_name_plural = "Compañias"

	def __str__(self):
		return self.nombre

class Titulo(models.Model):
	titulo = models.CharField(max_length=255)
	abreviatura = models.CharField(max_length=10, null=True, blank=True)

	class Meta:
		verbose_name = "Titulo"
		verbose_name_plural = "Titulos"

	def __str__(self):
		return self.titulo

class Individual(Compania):
	cedula = models.CharField(max_length=8, null=True, blank=True)
	tipo_direccion = models.CharField(max_length=255, null=True, blank=True, choices=TIPO_DIRECCION_CHOICE)
	puesto_trabajo = models.CharField(max_length=30, null=True, blank=True)
	titulo = models.ForeignKey(Titulo, blank=True, null=True, on_delete=models.SET_NULL)
	compania = models.ForeignKey(Compania, blank=True, null=True, on_delete=models.SET_NULL, related_name='relacion_compania')

	class Meta:
		verbose_name = "Individual"
		verbose_name_plural = "Individual"
	def __str__(self):
		if self.compania:
			return self.compania.nombre + ' ' + self.nombre
		else:
			return self.nombre