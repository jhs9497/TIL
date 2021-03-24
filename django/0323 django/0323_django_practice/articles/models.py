from django.db import models
from django.conf import settings

# User 모델을 가져오는 방법
# 1. get_user_model() => models.py 제외
# 2. settings.AUTH_USER_MODEL => models.py에서만 적용


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def __str__(self):
    #     pass

    def get_absolute_url(self):
        return f'/articles/{self.pk}/'


class Comment(models.Model):
    content = models.TextField(null=True)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)