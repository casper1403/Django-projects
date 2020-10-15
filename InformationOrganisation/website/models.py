from django.db import models

class BookModel(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=40,blank=True,null=True)
    authors = models.CharField(max_length=150,blank=True,null=True)
    original_publication_year = models.IntegerField(blank=True,null=True)
    original_title = models.CharField(max_length=150,blank=True,null=True)
    title = models.CharField(max_length=150,blank=True,null=True)
    average_rating = models.IntegerField()
    ratings_count = models.IntegerField()
    image_url = models.URLField()
    small_image_url = models.URLField()
    romance = models.IntegerField()
    scifi = models.IntegerField()
    adventure = models.IntegerField()
    action = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    mystery = models.IntegerField()
    supernatural = models.IntegerField()
    horror = models.IntegerField()
    historical = models.IntegerField()
    realistic = models.IntegerField()
    crime = models.IntegerField()
    comedy = models.IntegerField()
    war = models.IntegerField()
    manga_anime = models.IntegerField()
    sport = models.IntegerField()

    def __str__(self):
        return self.title


class GameModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,blank=True)
    romance = models.IntegerField()
    scifi = models.IntegerField()
    adventure = models.IntegerField()
    action = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    mystery = models.IntegerField()
    supernatural = models.IntegerField()
    horror = models.IntegerField()
    historical = models.IntegerField()
    realistic = models.IntegerField()
    crime = models.IntegerField()
    comedy = models.IntegerField()
    war = models.IntegerField()
    manga_anime = models.IntegerField()
    sport = models.IntegerField()

    def __str__(self):
        return self.name
