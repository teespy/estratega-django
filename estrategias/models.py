from django.db import models
from django.contrib.auth.models import User


class Estrategia(models.Model):
    dueno = models.ForeignKey(User, null=True)

    titulo = models.CharField(max_length=200, default='')

    # problematica es una sola
    problematica = models.TextField(default='')

    # causas pueden servarias, asi que se serializan en JSON
    # ver https://stackoverflow.com/questions/1110153/what-is-the-most-efficent-way-to-store-a-list-in-the-django-models
    causas = models.TextField(default='')


    def __str__(self):
        return self.titulo

    def has_problematica(self):
        if self.problematica == '':
            return False
        else:
            return True

    def has_causas(self):
        return False

    def has_solucionpolitica(self):
        return False

    def has_objetivos(self):
        return False

    def has_resultadosintermedios(self):
        return False

    def has_factoreshabilitantes(self):
        return False

    def has_barreras(self):
        return False

    def has_actoresrelevantes(self):
        return False


#class Problematica(models.Model):
#    estrategia = models.ForeignKey(Estrategia)
#    texto = models.TextField()
#
#    def __str__(self):
#        return self.texto


class Causa(models.Model):
    estrategia = models.ForeignKey(Estrategia)
    texto = models.TextField()

    def __str__(self):
        return self.texto


class SolucionPolitica(models.Model):
    estrategia = models.ForeignKey(Estrategia)
    texto = models.TextField()

    def __str__(self):
        return self.texto


class Objetivo(models.Model):
    estrategia = models.ForeignKey(Estrategia)
    texto = models.TextField()

    def __str__(self):
        return self.texto


class ResultadoIntermedio(models.Model):
    objetivo = models.ForeignKey(Objetivo)
    texto = models.TextField()

    def __str__(self):
        return self.texto


class FactorHabilitante(models.Model):
    objetivo = models.ForeignKey(Objetivo)
    texto = models.TextField()

    def __str__(self):
        return self.texto


class Barrera(models.Model):
    objetivo = models.ForeignKey(Objetivo)
    texto = models.TextField()

    def __str__(self):
        return self.texto


class ActorRelevante(models.Model):
    objetivo = models.ForeignKey(Objetivo)
    nombre = models.CharField(max_length=200)
    justificacion = models.TextField()

    def __str__(self):
        return self.nombre
