# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from profiles.models import Profile, UserType

admin.site.register(Profile)
admin.site.register(UserType)
