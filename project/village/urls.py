from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'job', views.JobViewSet, basename='job')
router.register(r'npc', views.NPCViewSet, basename='npc')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]