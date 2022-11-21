from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    start_at = models.DateTimeField()
    available_table = models.IntegerField()


class Table(models.Model):
    WARGAME = "WARGAME"
    BOARDGAME = "BOARDGAME"
    RPG = "RPG"
    CG = "CG"
    AUTRE = "AUTRE"

    EVENT_TYPE = (
        (WARGAME, "Wargame"),
        (BOARDGAME, "jeux de société"),
        (RPG, "jeux de rôle"),
        (CG, "jeux de cartes"),
        (AUTRE, "")
    )
    event_type = models.CharField(max_length=30, choices=EVENT_TYPE)
    description = models.CharField(max_length=200, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tables")
    available_sit = models.IntegerField()


class AssoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    payed = models.BooleanField()
