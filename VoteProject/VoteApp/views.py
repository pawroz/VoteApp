from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
	return render(request, 'VoteApp/detail.html', context)


def results(request, pk):
	try:
		specific_question = Question.objects.get(pk=pk)
		print(specific_question)
	except Question.DoesNotExist:
		raise Http404('Ankieta nie istnieje')

	context = {'specific_question':specific_question}
	return render(request, 'VoteApp/results.html', context)


def vote(request, pk):
	print(request.POST['choice'])
	try:
		specific_question = Question.objects.get(pk=pk)
	except Question.DoesNotExist:
		raise Http404('Ankieta nie istnieje')

	try:
		selected_choice = specific_question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'VoteApp/detail.html', {
			'specific_question': specific_question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('VoteApp:results', args=(specific_question.id,)))