from django.shortcuts import render
from rest_framework import viewsets
from .models import Flashcard, Collection
from .serializers import FlashcardSerializer, CollectionSerializer

# Create your views here.


class FlashcardView(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


class CollectionView(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
