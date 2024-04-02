from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserFile, UserPhoto
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Имя', required=False)
    last_name = forms.CharField(max_length=30, label='Фамилия', required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class FileForm(forms.ModelForm):

    class Meta:
        model = UserFile
        exclude = ['user_id']


class PhotoForm(forms.ModelForm):

    class Meta:
        model = UserPhoto
        exclude = ['user_id']
