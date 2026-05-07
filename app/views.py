from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AppUpdate
from .serializers import AppUpdateSerializer
from django.shortcuts import render

@api_view(['GET'])
def latest_update(request):
    latest = AppUpdate.objects.order_by('-version_code').first()
    serializer = AppUpdateSerializer(latest)
    return Response(serializer.data)

def app_update_list(request):
    apps = AppUpdate.objects.all().order_by('-version_code')
    return render(request, 'app_list.html', {'apps': apps})