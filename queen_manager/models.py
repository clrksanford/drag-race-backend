# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Queen(models.Model):
    name = models.CharField(max_length=200)
    winner = models.BooleanField()
    miss_congeniality = models.BooleanField()
    quote = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)

    def __str__(self):
        return '{0}'.format(self.name)
