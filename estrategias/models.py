from django.db import models
from django.contrib.auth.models import User


class Estrategia(models.Model):
    dueno = models.ForeignKey(User, null=True)
    titulo = models.CharField(max_length=200, default='')
    problematica = models.TextField(default='')
    causas = models.TextField(default='')
    solucionpolitica = models.TextField(default='')

    def __str__(self):
        return self.titulo

    def has_problematica(self):
        if self.problematica == '':
            return False
        else:
            return True

    def has_causas(self):
        if self.causas == '':
            return False
        else:
            return True

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

    def me_next(self):
        if not self.has_problematica():
            me_next = 'problematica'
        elif not self.has_causas():
            me_next = 'causas'
        elif not self.has_solucionpolitica():
            me_next = 'solucionpolitica'
        elif not self.has_objetivos():
            me_next = 'objetivos'
        elif not self.has_solucionpolitica():
            me_next = 'solucionpolitica'
        elif not self.has_objetivos():
            me_next = 'objetivos'
        elif not self.has_resultadosintermedios():
            me_next = 'resultadosintermedios'
        elif not self.has_factoreshabilitantes():
            me_next = 'factoreshabilitantes'
        elif not self.has_barreras():
            me_next = 'barreras'
        elif not self.has_actoresrelevantes():
            me_next = 'actoresrelevantes'
        else:
            me_next = False

        return me_next


class Objetivo(models.Model):
    estrategia = models.ForeignKey(Estrategia)
    objetivo = models.TextField()
    resultadosintermedios = models.TextField()
    factoreshabilitantes = models.TextField()
    barreras = models.TextField()
    barreras = models.TextField()

    def __str__(self):
        return self.objetivo
