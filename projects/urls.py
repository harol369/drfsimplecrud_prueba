from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/proyectos', ProjectViewSet, 'proyectos')

urlpatterns = router.urls