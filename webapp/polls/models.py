from django.db import models

import datetime
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # changing stuff to make a better representation of this object
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # same here!
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

