# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from core.models import TimestampedModel


class SabhaType(TimestampedModel):
    sabha_type = models.TextField(blank=False, unique=True)


class SabhaSessionManager(models.Manager):
    def active_session(self, sabha_type):
        return self.filter(status=sabha_type)


class SabhaSession(TimestampedModel):
    SABHA_SESSION_CHOICE = [
        ('active', 'active'),
        ('close', 'close'),
        ('pending', 'pending'),
        ('removed', 'removed'),
    ]

    objects = SabhaSessionManager()

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    sabhatype = models.ForeignKey('SabhaType', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, default=SABHA_SESSION_CHOICE[0][0], choices=SABHA_SESSION_CHOICE)
