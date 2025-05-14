# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Board(models.Model):

    #__Board_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    colour = models.CharField(max_length=255, null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    width = models.BooleanField()
    thickness = models.IntegerField(null=True, blank=True)
    availability = models.BooleanField()

    #__Board_FIELDS__END

    class Meta:
        verbose_name        = _("Board")
        verbose_name_plural = _("Board")



#__MODELS__END
