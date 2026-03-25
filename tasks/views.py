from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsTaskPermission


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskPermission]

    # Filtering & search (your existing code)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(
            Q(created_by=user) | Q(assigned_to=user)
        ).distinct()

    # Auto-set creator
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    # serializer permissions
    def get_serializer_context(self):
        return {'request': self.request}

    # Custom API: My Tasks
    @action(detail=False, methods=['get'], url_path='my-tasks')
    def my_tasks(self, request):
        tasks = Task.objects.filter(created_by=request.user)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    # Custom API: Assigned Tasks
    @action(detail=False, methods=['get'], url_path='assigned-tasks')
    def assigned_tasks(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
