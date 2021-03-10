from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # add가 붙으면 최초에만 들어감
    updated_at = models.DateTimeField(auto_now=True)  # add가 안붙으면 업데이트될 때 마다 값이 갱신됨
