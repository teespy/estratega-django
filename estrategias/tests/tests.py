from django.test import TestCase
from estrategias.models import Estrategia

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class EstrategiaTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user('prueba', password='prueba')
        self.usuario2 = User.objects.create_user('prueba2', password='prueba')

    def test_puedo_crear_estrategias(self):
        estrategia = Estrategia.objects.create(nombre="estrategia1", dueno=self.usuario)
        self.assertEquals(str(estrategia), "estrategia1")

    def test_obtener_estrategias_de_usuario(self):
        self.client.login(username='prueba', password='prueba')
        
        estrategia1 = Estrategia.objects.create(nombre="estrategia1", dueno=self.usuario)
        estrategia2 = Estrategia.objects.create(nombre="estrategia2", dueno=self.usuario)
        estrategia3 = Estrategia.objects.create(nombre="estrategia3", dueno=self.usuario2)

        url = reverse('estrategias:mis_estrategias')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

        self.assertIn(estrategia1, response.context['estrategias'].all())
        self.assertIn(estrategia2, response.context['estrategias'].all())

        self.assertNotIn(estrategia3, response.context['estrategias'].all())

    def test_redirige_a_home_si_usuario_no_esta_logeado(self):
        url = reverse('estrategias:mis_estrategias')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class HomeTestCase(TestCase):
    def setUp(self):
        pass

    def test_puedo_llegar_al_home(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
