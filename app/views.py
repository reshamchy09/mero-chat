from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AppUpdate
from .serializers import AppUpdateSerializer

@api_view(['GET'])
def latest_update(request):
    latest = AppUpdate.objects.order_by('-version_code').first()
    serializer = AppUpdateSerializer(latest)
    return Response(serializer.data)