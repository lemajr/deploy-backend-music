from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MusicRecommendationViewSet

# Create a router and register your viewset
router = DefaultRouter()
router.register(r'predict', MusicRecommendationViewSet, basename='predict_genre')

# Define the URLs
urlpatterns = router.urls
