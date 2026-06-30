from django.db import models

class paquetes(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=70)
    contenido= models.TextField()
    costo=models.PositiveIntegerField(verbose_name="Precio")
    imagen=models.ImageField(blank=True)
    imagen_movil=models.ImageField(blank=True)
    mensaje=models.TextField(verbose_name="Link a WhatsApp", blank=True)
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Paquete de graduación'
        verbose_name_plural='Paquetes de graduación'
    ordering=['nombre']
    def __str__(self):
        return self.nombre


class eventop(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=90)
    contenido= models.TextField()
    caption=models.TextField(verbose_name="Descripcion")
    generalidades=models.TextField()
    imagen= models.ImageField(blank=True)
    pronombre = models.CharField(default='')
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Evento'
        verbose_name_plural='Eventos'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre 
    
class serviciop(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=90)
    categoria=models.CharField(max_length=120, null=True, verbose_name="Categoría")
    total=models.PositiveIntegerField()
    precio=models.PositiveIntegerField()
    anchoin=models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ancho (pulgadas)", null=True, blank=True)
    altoin=models.DecimalField(verbose_name="Alto (pulgadas)", max_digits=5, decimal_places=2, null=True, blank=True)
    anchocm=models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ancho (cm)", null=True, blank=True) 
    altocm=models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Alto (cm)", null=True, blank=True)
    caption=models.TextField(verbose_name="Descripcion")
    generalidades=models.TextField(verbose_name="Link a WhatsApp")
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre 
    
class serviciopop(models.Model):
    id= models.AutoField(primary_key=True)
    foto= models.ImageField(blank=True)
    nombre=models.ForeignKey(serviciop, on_delete=models.CASCADE)
    categoria=models.CharField(max_length=120, null=True, verbose_name="Categoría",blank=True)
    precio=models.PositiveIntegerField(null=True,blank=True)
    caption=models.TextField(verbose_name="Descripcion")
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Servicio destacado'
        verbose_name_plural='Servicios populares'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre.nombre
    
    def save(self,*args,**kwargs):
        if self.nombre:
            self.precio = self.nombre.precio
            self.categoria = self.nombre.categoria
    
        super().save(*args, **kwargs)