#created manually
from django import forms
from .models import Post, Comment, UserRegistration
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class RegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', )