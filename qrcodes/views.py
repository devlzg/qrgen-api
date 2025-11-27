from rest_framework import viewsets
from .models import QRCode
from .serializers import QRCodeSerializer

class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all() # select *
    serializer_class = QRCodeSerializer