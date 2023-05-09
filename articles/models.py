from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    
    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    articles = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    comments= models.CharField(max_length=200)

    def __str__(self):
        return self.comments
    
    def get_absolute_url(self):
        return reverse("article_list")
    