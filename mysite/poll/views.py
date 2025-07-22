from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

def index(request):
    latest_question_list = Question.object.order_by("-pub_data")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)


def result(request, question_id):
    response = " These are the responses to the question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        # where is .choice_set coming from
    except (KeyError, Choice.DoesNotExist):
        # pycharm is telling me Choice is unresolved reference,
        # but I assumed it was a reference to something in the database
        return render(request, "polls/details.html", {"question":question,"error message":"You didn't select a choice.",},)
        # long as hell, but apparently the exception should still return a specified error message
    else:
        selected_choice.votes = F("Votes") + 1
        selected_choice.save()