from django.shortcuts import render

# Create your views here.
from LibraryBook.models import Library
from LibraryBook.serializers import LibrarySerializer
from rest_framework import viewsets

# authentication
# from rest_framework.permissions import IsAuthenticated,IsAdminUser

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class LibraaryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)