from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests
from rest_framework import status
from rest_framework.views import APIView
from core.models import Account
from django.shortcuts import get_object_or_404
from rest_framework import generics
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    @action(detail=False, methods=['get'])
    def by_account(self, request, *args, **kwargs):
        account_id = request.query_params.get('account_id')
        if not account_id:
            return Response({"error": "account_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        destinations = Destination.objects.filter(account__account_id=account_id)
        serializer = self.get_serializer(destinations, many=True)
        return Response(serializer.data)

class DataHandlerViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def incoming_data(self, request, *args, **kwargs):
        app_secret_token = request.headers.get('CL-X-TOKEN')
        if not app_secret_token:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            account = Account.objects.get(app_secret_token=app_secret_token)
        except Account.DoesNotExist:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        destinations = account.destinations.all()

        for destination in destinations:
            headers = destination.headers
            if destination.http_method.lower() == 'get':
                response = requests.get(destination.url, headers=headers, params=data)
            else:
                response = requests.request(destination.http_method.lower(), destination.url, headers=headers, json=data)
        
        return Response({"status": "success"}, status=status.HTTP_200_OK)



class DestinationListAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationByAccountAPIView(generics.ListAPIView):
    serializer_class = DestinationSerializer

    def get_queryset(self):
        account_id = self.kwargs['account_id']
        account = get_object_or_404(Account, account_id=account_id)
        return Destination.objects.filter(account=account)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)