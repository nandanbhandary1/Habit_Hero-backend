from rest_framework import viewsets
from .models import Habit, CheckIn
from .serializers import HabitSerializer, CheckInSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all().order_by("id")
    serializer_class = HabitSerializer


class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all().order_by("id")
    serializer_class = CheckInSerializer
