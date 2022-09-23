import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """Class for create poll question."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date', null=True)

    def __str__(self):
        """represents the class objects as a string."""
        return self.question_text

    def was_published_recently(self):
        """Return true if the question was recently published."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """Returns True if current date is
        on or after question’s publication date."""
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """Returns True if voting is allowed for this question."""
        if self.end_date is True:
            return self.is_published and timezone.now() <= self.end_date
        return self.is_published()


class Choice(models.Model):
    """Class for create question choices."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """represents the class objects as a string."""
        return self.choice_text

    @property
    def votes(self) -> int:
        """Return votes amount of that choice."""
        return Vote.objects.filter(choice=self).count()


class Vote(models.Model, ):
    user = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE)
    choice = models.ForeignKey(
        Choice, blank=False, null=False, on_delete=models.CASCADE)

    @property
    def question(self):
        return self.choice.question
