from rest_framework import serializers
from .models import Tour, Award, Advantage, About, Contact


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'name', 'image', 'price']


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = ['id', 'name', 'image', 'text']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'phone', 'email', 'address', 'link']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'image', 'text', 'clients', 'experience', 'progress']


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id', 'image']


class LeadSerializer(serializers.Serializer):
    tour_id = serializers.IntegerField()
    name = serializers.CharField()
    phone = serializers.CharField()
