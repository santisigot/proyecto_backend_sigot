from django.db import models


class Dragonball(models.Model):
    name = models.CharField(max_length=128)
    ki = models.IntegerField()
    raza = models.CharField(max_length=128)
    años = models.IntegerField()


    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Dragonballsaga(models.Model):
    name = models.CharField(max_length=128)
    saga = models.CharField(max_length=100, default="todas")
    capitulos = models.IntegerField()
    villano = models.BooleanField(default=False)
    transformaciones = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Dragonballvivo(models.Model):
    name = models.CharField(max_length=128)
    vivo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'
    


class User(models.Model):
    name = models.CharField(max_length=128)
    dragonballs = models.ManyToManyField(Dragonball, blank=True)
    dragonballsagas = models.ManyToManyField(Dragonballsaga, blank=True)
    dragonballvivos = models.ManyToManyField(Dragonballvivo, blank=True)

    def __str__(self):
        return self.name
    

    




