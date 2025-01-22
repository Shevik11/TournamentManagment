from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('player', 'Player'),
    ]
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    choices = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Tournament(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_b')
    date = models.DateField()
    score_a = models.IntegerField()
    score_b = models.IntegerField()

    def __str__(self):
        return f"{self.team_a.name } {self.score_a }  vs {self.score_b} { self.team_b.name}"

class TournamentTable(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} ({self.tournament.name})"