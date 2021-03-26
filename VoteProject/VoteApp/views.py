from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import JsonResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *


def home(request):

    context = {}
    return render(request, 'VoteApp/home.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('VoteApp:loginPage')

    context = {'form': form, }
    return render(request, 'VoteApp/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('VoteApp:home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'VoteApp/login.html', context)


def logoutUser(request):

    logout(request)
    return redirect('VoteApp:loginPage')


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_questions': latest_questions}
    return render(request, 'VoteApp/index.html', context)


def detail(request, pk):
    try:
        specific_question = Question.objects.get(pk=pk)

    except Question.DoesNotExist:
        raise Http404('Ankieta nie istnieje')

    context = {'specific_question': specific_question}
    return render(request, 'VoteApp/detail.html', context)


def results(request, pk):
    try:
        specific_question = Question.objects.get(pk=pk)
        print(specific_question)
    except Question.DoesNotExist:
        raise Http404('Ankieta nie istnieje')

    context = {'specific_question': specific_question}
    return render(request, 'VoteApp/results.html', context)


def vote(request, pk):
    print(request.POST['choice'])
    try:
        specific_question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404('Ankieta nie istnieje')

    try:
        selected_choice = specific_question.choice_set.get(
            pk=request.POST['choice'])
    except (Choice.DoesNotExist):

        return render(request, 'VoteApp/detail.html', {
            'specific_question': specific_question,
            'error_message': "You didn't select a choice.",
        })

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('VoteApp:results', args=(specific_question.id,)))


def resultsData(request, pk):
    voteData = []

    question = Question.objects.get(id=pk)
    votes = question.choice_set.all()

    for i in votes:
        voteData.append({i.choice: i.votes})

    print(voteData)
    return JsonResponse(voteData, safe=False)
