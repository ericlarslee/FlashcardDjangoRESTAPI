from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, blank=True, default=None)
