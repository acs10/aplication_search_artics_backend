from rest_framework import serializers
from .models import UserProfile, SearchHistory

class UserProfileSerializer(serializers.ModelSerializer):
        
    class Meta: 
        fields = ('id','user','name','email','telephone','state','city','country','age','occupation','interest')
        model = UserProfile

class SearchHistorySerializer(serializers.ModelSerializer):
        
    class Meta: 
        fields = ('id','user','query','sort_by_date','language','period_start','period_end','timestamp')
        model = SearchHistory



