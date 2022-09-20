from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Choice, Question, Vote
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    """This class is for display the question"""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    """This class is for display each question"""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, *args, **kwargs):
        """To back to index page if not found"""
        try:
            question = get_object_or_404(Question, pk=kwargs['pk'])
        except Http404:
            messages.error(
                request, "Question is not available")
        if not question.can_vote():
            messages.error(request, "Question is not available")
            return HttpResponseRedirect(reverse('polls:index'))
        return super().get(request, *args, **kwargs)



class ResultsView(generic.DetailView):
    """This class is for display each question's result"""
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    """process of voting"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            vote = Vote.objects.get(user=request.user, choice__question=question)
            if vote:
                vote.choice = selected_choice
                vote.save()
        except Vote.DoesNotExist:
            new_vote = Vote.objects.create(user=request.user, choice=selected_choice)
            new_vote.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def reverse_to_poll(self):
    """redirect to homepage"""
    return HttpResponseRedirect(reverse('polls:index'))








