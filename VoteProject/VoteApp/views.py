from django.shortcuts import render

from .models import *


def index(request):
	latest_questions = Question.objects.order_by('-pub_date')[:5]


	context = {'latest_questions':latest_questions}
	return render(request,'VoteApp/index.html', context)


def detail(request, pk):
	try:
		specific_question = Question.objects.get(pk=pk)
	except Question.DoesNotExist:
		raise Http404('Ankieta nie istnieje')




	context = {'specific_question':specific_question}
	return render(render, 'VoteApp/results.html', context)


def results(request, pk):
	try:
		specific_question = Question.objects.get(pk=pk)
	except Question.DoesNotExist:
		raise Http404('Ankieta nie istnieje')

	context = {'specific_question':specific_question}
	return render(render, 'VoteApp/results.html', context)


