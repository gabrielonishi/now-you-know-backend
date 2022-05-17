from unicodedata import name
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def setRating(self, avg_rat):
        self.average_rating = avg_rat
    
    @staticmethod
    def normalize_name(name:str):
        # Deixar todos os nomes em letras minúsculas
        lower_name = name.lower()
        # Separar nomes em uma lista
        name_list = lower_name.split()
        # Juntando
        normalized = "_".join(name_list)
        return normalized

class UserTry(models.Model):
    score = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.artist}, {self.score} points'
    
    class Meta:
        ordering = ['score']