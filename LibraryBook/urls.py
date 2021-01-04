from django.urls import path,include
from LibraryBook import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('lab', views.LibraaryViewSet)

urlpatterns = [
    path('',include(router.urls))
]