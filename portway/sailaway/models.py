from django.db import models

# Create your models here.
class Port(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Sailaway(models.Model):
    origin = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name="arrival")
    duration = models .IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    sailaways = models.ManyToManyField(Sailaway, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"