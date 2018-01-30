from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import SignUpForm, VotingForm
from .models import Candidate

# Create your views here.
@login_required
def index(request):
    user = Candidate.objects.order_by('id')
    form = VotingForm()
    context = {'user': user, 'form': form}
    return render(request, 'registration/index.html', context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
            
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@require_POST
def vote_candidate(request):
    form = VotingForm(request.POST) 

    if form.is_valid():
        try:
            candidate = Candidate.objects.get(name__iexact=form.cleaned_data['name'])
        except Candidate.DoesNotExist:
            return HttpResponse('invalid name')
        else:
            candidate.score += 10
            candidate.save()
            request.user.vote_status = True
            print('user voting status is {}'.format(request.user.vote_status))
            request.user.save()
            print('user voting status is {}'.format(request.user.vote_status))
            return redirect('index')
    else:
        form = VotingForm()
