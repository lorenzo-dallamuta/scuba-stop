from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext as _
from crispy_forms.layout import ButtonHolder, Fieldset, Layout, Submit
from accounts.models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label=_('Username'))
    password = forms.CharField(
        widget=forms.PasswordInput(), label=_('Password'))
    fields = ('username', 'password')

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
                Submit('submit', _('Login'), css_class='btn-success')
            ))

    def get_user(self):
        username = self.cleaned_data.get('username').strip()
        password = self.cleaned_data.get('password')
        return authenticate(username=username, password=password)


class SignupFormUser(UserCreationForm):
    # this is to reset Null and Blank to false
    first_name = forms.CharField(max_length=50, label=_('First Name'))
    last_name = forms.CharField(max_length=50, label=_('Last Name'))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


# class UpdateFormUser(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('email',)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
class UpdateFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class SignupFormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
