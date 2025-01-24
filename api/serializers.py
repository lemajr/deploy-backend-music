# from rest_framework import serializers

# from .models import Item

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ('id', 'name', 'description')  # '__all__'


from rest_framework import serializers

class MusicRecommendationSerializer(serializers.Serializer):
    gender = serializers.ChoiceField(choices=["male", "female"], required=True)
    age = serializers.IntegerField(min_value=0, required=True)
