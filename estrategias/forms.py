from django.core.urlresolvers import reverse
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import FormActions

from django.contrib.auth.forms import AuthenticationForm

from django.core.exceptions import ValidationError

from .models import Estrategia


class EstrategiaLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super(EstrategiaLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                                Field('username', css_class='input-xlarge'),
                                Field('password', css_class='input-xlarge')
        )  


class EstrategiaTituloForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        fields = ('titulo',)

    def __init__(self, *args, **kwargs):
        super(EstrategiaTituloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                                Field('titulo', css_class='input-xlarge'),
        )  

    titulo = forms.CharField(label='Esta es una estrategia para...', max_length=80)


class EstrategiaProblematicaForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        fields = ('problematica',)

    def __init__(self, *args, **kwargs):
        super(EstrategiaProblematicaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper() 
        self.helper.layout = Layout(
                                Field('problematica', css_class='input-xlarge'),
        )  

    problematica = forms.TextInput()