from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, CheckInViewSet

router = DefaultRouter()
router.register(r"habits", HabitViewSet)
router.register(r"checkins", CheckInViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
