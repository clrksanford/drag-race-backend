# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import QueenSerializer
from .models import Queen

# Create your views here.
class QueenViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows you to view queens
    """
    queryset = Queen.objects.all()
    serializer_class = QueenSerializer
