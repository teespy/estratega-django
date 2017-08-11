from django.test import TestCase
from estrategias.models import Estrategia

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class EstrategiaTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user('prueba', password='prueba')
        self.usuario2 = User.objects.create_user('prueba2', password='prueba')

    def test_puedo_crear_estrategias(self):
        estrategia = Estrategia.objects.create(titulo="estrategia1", dueno=self.usuario)
        self.assertEquals(str(estrategia), "estrategia1")

    def test_obtener_estrategias_de_usuario(self):
        self.client.login(username='prueba', password='prueba')
        
        estrategia1 = Estrategia.objects.create(titulo="estrategia1", dueno=self.usuario)
        estrategia2 = Estrategia.objects.create(titulo="estrategia2", dueno=self.usuario)
        estrategia3 = Estrategia.objects.create(titulo="estrategia3", dueno=self.usuario2)

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

    def test_usuario_tiene_estrategias(self):
        self.assertLess(Estrategia.objects.filter(dueno=self.usuario).count(), 1)

        estrategia1 = Estrategia.objects.create(titulo="estrategia1", dueno=self.usuario)        
        self.assertEqual(Estrategia.objects.filter(dueno=self.usuario).count(), 1)


class UserTestCase(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user('prueba@prueba.com', password='prueba')

    def test_log_in_successful_redirige_a_estrategias(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'prueba@prueba.com', 'password': 'prueba'})

        self.assertRedirects(response, reverse('estrategias:mis_estrategias'))

    def test_log_in_unsuccessful_redirige_a_estrategias(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'noexiste', 'password': 'noexiste'})

        self.assertRedirects(response, reverse('index'))


class FormTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_form_nueva_estrategia_correcto_redirige_a_definir_problematica(self):
        url = reverse('estrategias:nueva_estrategia')
        response = self.client.post(url, {'titulo': 'Nueva Estrategia'})

        self.assertRedirects(response, reverse('estrategias:problematica'))

    def test_form_nueva_estrategia_incorrecto_redirige_a_mis_estrategias(self):
        url = reverse('estrategias:nueva_estrategia')
        response = self.client.post(url, {'titulo': 'hgfh fgh fgh gf hfg hfg hf hgfMuchos caracteres jdsa dahkw hd khwak dhwakjh dkawh dkjha kjhwakh dkajwh djkawh djkawh jkhdkwjah kjawh k'})

        self.assertRedirects(response, reverse('estrategias:nueva_estrategia'))
