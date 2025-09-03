from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, SkillViewSet, ProjectViewSet, health, skills_top, search

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"skills", SkillViewSet)
router.register(r"projects", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("health/", health),
    path("skills/top/", skills_top),
    path("search/", search),
]
