from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50)
    optionA = models.TextField()
    optionB = models.TextField()
    left = models.IntegerField(null=True)
    right = models.IntegerField(null=True)


class Like(models.Model):
    count = models.ForeignKey("Game", on_delete=models.CASCADE)


