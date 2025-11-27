from rest_framework import serializers
from .models import QRCode

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = QRCode
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']