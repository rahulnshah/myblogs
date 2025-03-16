from django import forms
from .models import Post, CodeSnippet

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

# this will be my search box 
class NameForm(forms.Form):
    your_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'form-control me-2', 'type' : 'search', 'placeholder': 'type something...', 'aria-label' : 'Search'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))