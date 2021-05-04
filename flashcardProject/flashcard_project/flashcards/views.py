from django.shortcuts import render
from rest_framework import viewsets
from .models import Flashcard
from .serializers import FlashcardSerializer

# Create your views here.


class FlashcardView(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
