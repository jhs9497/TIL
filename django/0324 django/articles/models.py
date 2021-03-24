from django.db import models

# Create your models here.
class Article(models.Model):
    # 1: Parent Table
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(models.Model):
    # N: Child Table
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # article의 pk 저장 / on_delete=models.CASCADE -> 게시글이 지워져서 해당 pk가 없어졌을 때 오류가 나지 않게 하기위함
    # 게시글이 지워질 때 해당되는 댓글도 삭제한다!



