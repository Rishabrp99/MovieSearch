from django.db import models

# Create your models here.
class Data(models.Model):
    movie_name=models.CharField(max_length=100)
    actor_name=models.CharField(max_length=100)
    actress_name=models.CharField(max_length=100)
    director_name=models.CharField(max_length=100)
    year=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.movie_name