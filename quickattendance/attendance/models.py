# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from core.models import TimestampedModel


class SabhaType(TimestampedModel):
    sabha_type = models.TextField(blank=False, unique=True)
