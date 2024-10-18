from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input_login_block1', 'placeholder' : 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input_login_block', 'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input_login_block', 'placeholder': 'Имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input_login_block', 'placeholder': 'E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input_login_block0', 'placeholder': 'Придумайте и введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input_login_block0', 'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'image-upload'}))
 #   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-group2', 'readonly': True}))

    class Meta:
        model = User
        fields = ('image',)
