from django.db import models  

class Player(models.Model):
    name = models.CharField(max_length=200)
    

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    players = models.ManyToManyField(Player)

    
class Game(models.Model):
    first_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="first_player")
    second_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="second_player")
    first_player_goals = models.IntegerField(blank=True, null=True)
    second_player_goals = models.IntegerField(blank=True, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    