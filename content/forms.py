from django import forms
from .models import Content, ContentDetail

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title']

class ContentDetailForm(forms.ModelForm):
    class Meta:
        model = ContentDetail
        fields = ['text_content', 'image_content', 'video_content', 'pdf_content', 'word_content', 'audio_content']
