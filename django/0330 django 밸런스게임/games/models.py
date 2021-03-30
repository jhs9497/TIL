from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    optionA = models.TextField()
    optionA_image = models.ImageField(upload_to='games/', blank=True)
    optionB = models.TextField()
    optionB_image = models.ImageField(upload_to='games/', blank=True)
    # left = models.IntegerField(null=True)
    # right = models.IntegerField(null=True)


class Like(models.Model):
    number = models.ForeignKey("Game", on_delete=models.CASCADE)
    optionA = models.IntegerField(default=0)
    optionB = models.IntegerField(default=0)


