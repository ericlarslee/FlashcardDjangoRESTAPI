from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('flashcards', views.FlashcardView)
router.register('collections', views.CollectionView)

urlpatterns = [
    path('', include(router.urls))
]
