from django.forms import ModelForm, modelform_factory, Form, modelformset_factory
from django import forms
from django.contrib.auth.models import User

from .models import Task

class SearchForm(forms.Form):
    q = forms.CharField(max_length=20, label='Поиск по словам')


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', required=False, widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(label='Пароль (повторно)', initial='начальное значение', required=False)
    regex_field = forms.RegexField(r'^U[a-zA-Z]{4}$')
    is_client = forms.BooleanField()
    rate = forms.FloatField()
    number_of_goods = forms.IntegerField(widget=forms.widgets.NumberInput())
    desired_date = forms.DateField(widget=forms.widgets.DateInput())
    choice = forms.ChoiceField(choices=(('f', 'first'), ('s', 'second')))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')


class TaskForm(ModelForm):
    title = forms.CharField(label='Тема задачи')
    content = forms.CharField(label='Содержание задачи ',widget=forms.widgets.Textarea())
    task_id = forms.ModelChoiceField(label='Задачи', widget=forms.widgets.Select(attrs={'size': 2}), queryset=Task.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
