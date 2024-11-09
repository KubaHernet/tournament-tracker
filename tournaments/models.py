from django.db import models  


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name #test3

    
class Game(models.Model):
    first_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="first_player")
    second_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="second_player")
    first_player_goals = models.IntegerField(blank=True, null=True)
    second_player_goals = models.IntegerField(blank=True, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_player.name} {self.first_player_goals or '_'}:{self.second_player_goals or '_'} {self.second_player.name}"

    def is_finished(self):
        return self.first_player_goals is not None and self.second_player_goals is not None

