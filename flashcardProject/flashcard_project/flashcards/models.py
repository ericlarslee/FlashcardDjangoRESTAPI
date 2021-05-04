from django.db import models


class Flashcard(models.Model):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
#   collection =