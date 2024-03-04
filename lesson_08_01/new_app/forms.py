from django.forms import ModelForm, modelform_factory, Form, modelformset_factory
from django import forms
from django.contrib.auth.models import User

from .models import Author, Post, Category


AuthorFormset = modelformset_factory(Author, fields='__all__')


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


AuthorForm = modelform_factory(Author, fields=['name', 'bio'])
# 1) model (Author)
# 2) fields ['name', 'email'] / '__all__' ; exclude ['email']


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         labels = {'title': 'Название поста',
#                   'content': "Содержание поста",
#                   'views': 'Количество просмотров',
#                   'status': 'Статус'}
#         help_text = {'categories': 'Выберете категории, к которым относится ваш пост'}
#         widgets = {'author_id': Select(attrs={'size': 5})} # <select></select>


class PostForm(ModelForm):
    title = forms.CharField(label='Название поста')
    content = forms.CharField(label='Содержание поста', widget=forms.widgets.Textarea())
    author_id = forms.ModelChoiceField(label='Автор', widget=forms.widgets.Select(attrs={'size': 2}), queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = '__all__'


# label - надпись для поля
# label_suffix - дополнительный поясняющий текст
# initial
# required: bool
# widget - выбор тега HTML, который будет отвечать за заполнение поля
# validators - список программных модулей, которые проверяют верность заполнения поля
# disabled

# CharField(min_length, max_length, strip)
# EmailField
# RegexField
# IntegerField
# FolatField
# DateTimeField
# ModelChoiceField
# ModelMultipleChoiceField
# ChoiceField
# MultipleChoiceField

# Widgets == HTML tag
# TextInput
# NumberInput
# EmailInput
# PasswordInput
# DateInput


class CategoryForm(forms.ModelForm):


    class Meta:
        fields = '__all__'
        model = Category
