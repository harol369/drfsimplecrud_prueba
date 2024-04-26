from rest_framework import viewsets, permissions
from .models import Proyectos
from .serializers import ProyectoSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializer
