from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full pl-10 pr-4 py-3 text-sm bg-white border border-charcoal-200 rounded-xl text-charcoal-800 placeholder-charcoal-400 focus:outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 transition-all duration-300',
            'placeholder': 'email@dahana.id'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full pl-10 pr-10 py-3 text-sm bg-white border border-charcoal-200 rounded-xl text-charcoal-800 placeholder-charcoal-400 focus:outline-none focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 transition-all duration-300',
            'placeholder': 'Masukkan password'
        })
    )


ICON_FIELDS = {'email', 'username', 'phone', 'role'}

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'role', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            padding = 'pl-10' if name in ICON_FIELDS else 'pl-3'
            field.widget.attrs.update({'class': f'w-full {padding} pr-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'role', 'phone', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            padding = 'pl-10' if name in ICON_FIELDS else 'pl-3'
            field.widget.attrs.update({'class': f'w-full {padding} pr-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})
