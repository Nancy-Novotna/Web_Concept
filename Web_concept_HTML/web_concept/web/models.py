from django.db import models

# Create your models here.
class Game(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField('Genre', related_name='games')
    release_date = models.DateField()
    developer = models.ManyToManyField('Developer', related_name='games')
    publisher = models.ManyToManyField('Publisher', related_name='games')
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Developer(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    hq = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    hq = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Achievement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='achievements')
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.IntegerField()
    img = models.ImageField(upload_to='achievements/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.game.title})"
    
class Timeline(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='timelines')
    event = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.event} ({self.game.title})"
    
class Character(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    img = models.ImageField(upload_to='characters/')
    description = models.TextField()
    screen_time = models.IntegerField()
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.game.title})"
    
class Screenshot(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='screenshots')
    img = models.ImageField(upload_to='screenshots/')

    def __str__(self):
        return f"Screenshot of {self.game.title}"