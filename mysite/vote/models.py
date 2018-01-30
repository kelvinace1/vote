from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=25)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

class VotingStatus(models.Model):
    status = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_status = models.BooleanField(default=False)


    def __str__(self):
        return "{}".format(self.status)



