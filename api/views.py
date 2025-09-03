from django.db.models import Count, Q
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .models import Profile, Skill, Project
from .serializers import ProfileSerializer, SkillSerializer, ProjectSerializer


@api_view(["GET"])
def home(request):
    if request.accepted_renderer.format == "json":
        return Response({"message": "API is running!"})
    
    return render(request, "index.html")
    
def frontend(request):
    return render(request, "index.html")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["id", "name", "email"]
    ordering = ["id"]
    search_fields = ["name", "email", "summary"]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["id", "name", "level"]
    ordering = ["-level"]
    search_fields = ["name"]

    def create(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return super().create(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().prefetch_related("skills", "profile")
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["id", "title"]
    ordering = ["id"]
    search_fields = ["title", "description"]

    def list(self, request, *args, **kwargs):
        skill = request.query_params.get("skill")
        if skill:
            qs = self.queryset.filter(skills__name__icontains=skill).distinct()
        else:
            qs = self.queryset

        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def skills_top(request):
    top = (
        Skill.objects.annotate(project_count=Count("projects"))
        .order_by("-project_count", "-level")[:10]
    )
    data = [
        {"name": s.name, "level": s.level, "projects": s.project_count}
        for s in top
    ]
    return Response(data)


@api_view(["GET"])
def search(request):
    q = request.query_params.get("q", "").strip()
    if not q:
        return Response({"projects": [], "skills": [], "profiles": []})

    proj = Project.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q) |
        Q(skills__name__icontains=q)
    ).distinct()

    skl = Skill.objects.filter(name__icontains=q).distinct()

    prof = Profile.objects.filter(
        Q(name__icontains=q) |
        Q(summary__icontains=q) |
        Q(education__icontains=q)
    ).distinct()

    return Response({
        "projects": ProjectSerializer(proj, many=True).data,
        "skills": SkillSerializer(skl, many=True).data,
        "profiles": ProfileSerializer(prof, many=True).data,
    })


