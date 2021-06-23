from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, Layout, Submit
from accounts.models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    fields = ['username', 'password']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_id = 'id-login-form'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset('Login', 'username', 'password',
                     style='color:green;'),
            ButtonHolder(
                Submit('submit', 'Login', css_class='btn-success')
            ))

    def get_user(self):
        username = self.cleaned_data.get('username').strip()
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)


class SignupFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name')


class SignupFormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
