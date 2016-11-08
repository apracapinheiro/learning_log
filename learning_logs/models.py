# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Um assunto sobre o qual o usário está aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text


class Entry(models.Model):
    """Algo específico sobre um assunto"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Entries"


    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text[:50] + "..."