from rest_framework import serializers
from .models import Flashcard, Collection


class FlashcardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['url', 'id', 'question', 'answer', 'collection']


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ['url', 'id', 'name']
