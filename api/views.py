# from rest_framework import viewsets
# from .models import Item
# from.serializers import ItemSerializer

# # Create your views here.
# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

    
import os
import joblib
import numpy as np
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicRecommendationSerializer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "music-recommender.joblib")  

# Load the pre-trained model
model = joblib.load(MODEL_PATH)

try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully!")
except FileNotFoundError as e:
    print(f"Error: {e}")


class MusicRecommendationViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = MusicRecommendationSerializer(data=request.data)

        # Validate the input
        if serializer.is_valid():
            validated_data = serializer.validated_data
            gender = validated_data["gender"]
            age = validated_data["age"]

            # Map gender to binary value (male = 1, female = 0)
            gender_value = 1 if gender == "male" else 0

            # Prepare input for the model
            input_data = np.array([[age, gender_value]])


            # Predict the genre
            prediction = model.predict(input_data)

            return Response({"predicted_genre": prediction[0]}, status=status.HTTP_200_OK)

        # If validation fails, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
