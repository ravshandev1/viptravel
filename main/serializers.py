from rest_framework import serializers
from .models import Tour, Award, Advantage, About, Contact


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class LeadSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
