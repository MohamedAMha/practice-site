from django.db import models
from django.utils import timezone
import datetime

# Purpose of models is to define metadata so that db can store information for the site, I guess?
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")
    def __str__(self):
        return self.question_text  # so when question object is called, it doesn't return memory address
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
        # if I'm not expected to memorize, where do I pull the list of attributes for models.
        # also what does .ForeignKey() mean or do
    choice_text = models.CharField(max_length=200)  # anytime I wanted text, I have to use models.Chafield
    votes = models.IntegerField(default=0)  # Integerfield to represent number of votes
    def __str__(self):
        return self.choice_text


