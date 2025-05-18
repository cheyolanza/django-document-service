from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import GreetView, DocumentViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path("greet/", GreetView.as_view(),name="greet"),
    path('',include(router.urls)),
]
