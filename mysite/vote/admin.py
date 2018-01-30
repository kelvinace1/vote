from django.contrib import admin
from .models import Candidate, VotingStatus

# Register your models here.


admin.site.register(Candidate)

admin.site.register(VotingStatus)
