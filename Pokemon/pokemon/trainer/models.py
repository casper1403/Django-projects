from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Pokemon(models.Model):

    legendary = [(0,'0'),(1,'1')]
    name = models.CharField(max_length=50)
    pokedex_number = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    hp = models.IntegerField()
    base_happiness = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    is_legendary = models.IntegerField(choices=legendary)
    capture_rate = models.IntegerField()


class Profile(models.Model):

    user = models.OneToOneField(User,related_name="Profile", related_query_name="Profile", on_delete=models.CASCADE)
    trainername = models.CharField(max_length=40, blank = True, null = True)
    points = models.IntegerField(blank = True, null = True)
    pokemon = models.ManyToManyField(Pokemon)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Profile.save()
