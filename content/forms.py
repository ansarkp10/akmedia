from django import forms
from .models import Content, ContentDetail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title']

class ContentDetailForm(forms.ModelForm):
    class Meta:
        model = ContentDetail
        fields = ['text_content', 'image_content', 'video_content', 'pdf_content', 'word_content', 'audio_content']
