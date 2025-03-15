from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:  # helper class 
        model = Post
        fields = ['title', 'text', 'codeText'] #  once again we will create a link to the forms page, a URL, a view and a template

# this will be my search box 
class NameForm(forms.Form):
    your_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'form-control me-2', 'type' : 'search', 'placeholder': 'type something...', 'aria-label' : 'Search'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))