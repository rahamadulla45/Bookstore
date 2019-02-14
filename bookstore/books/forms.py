from books.models import Book
from django import forms
from django.contrib.auth.models import User


class CreateForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())