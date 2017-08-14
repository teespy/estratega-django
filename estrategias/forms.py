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
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('login')
        self.helper.form_class='form-login'
        self.helper.layout = Layout(
                                Field('username', css_class='input-xlarge'),
                                Field('password', css_class='input-xlarge'),
                                FormActions(
                                    Submit('save_changes', 'Ingresar', css_class="btn-primary")
                                )
        )  

    def confirm_login_allowed(self, user):
        pass


class EstrategiaTituloForm(forms.ModelForm):
    class Meta:
        model = Estrategia
        exclude = ('dueno',)
        #fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EstrategiaTituloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('estrategias:nueva_estrategia')
        self.helper.form_class='form-estrategia'
        self.helper.layout = Layout(
                                Field('titulo', css_class='input-xlarge'),
                                FormActions(
                                    Submit('save_changes', 'Comenzar!', css_class="btn-primary"), css_class="text-center p-vrt-20"
                                )
        )  

    titulo = forms.CharField(label='Esta es una estrategia para solucionar...', max_length=100)

