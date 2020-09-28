from django.db import models
from trainer.models import Profile, Pokemon
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class PokemonStats(Pokemon):
    is_alive = True

class Hunters(models.Model):
    user = models.OneToOneField(User, related_name="Hunters", related_query_name="Hunters", on_delete=models.CASCADE)
    pokemon = models.ManyToManyField(Pokemon)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Hunters.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Hunters.save()
