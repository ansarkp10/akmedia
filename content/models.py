from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

class ContentDetail(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='details')
    text_content = models.TextField(blank=True, null=True)
    image_content = models.ImageField(upload_to='images/', blank=True, null=True)
    video_content = models.FileField(upload_to='videos/', blank=True, null=True)
    pdf_content = models.FileField(upload_to='pdfs/', blank=True, null=True)
    word_content = models.FileField(upload_to='words/', blank=True, null=True)
    audio_content = models.FileField(upload_to='audios/', blank=True, null=True)
