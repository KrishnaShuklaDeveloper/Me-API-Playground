from rest_framework import serializers
from .models import Profile, Skill, Project

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "level"]


class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    skills_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Skill.objects.all(),
        source="skills"
    )

    class Meta:
        model = Project
        fields = ["id", "title", "description", "links", "skills", "skills_ids", "profile"]


class ProfileSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "email",
            "education",
            "summary",
            "links",
            "skills",
            "projects",
        ]

    def create(self, validated_data):
        projects_data = validated_data.pop('projects', [])
        profile = Profile.objects.create(**validated_data)

        for project_data in projects_data:
            skills_ids = project_data.pop('skills_ids', [])
            project = Project.objects.create(profile=profile, **project_data)
            project.skills.set(skills_ids)

        return profile

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr != "projects":
                setattr(instance, attr, value)
        instance.save()

        projects_data = validated_data.get('projects', [])
        for project_data in projects_data:
            skills_ids = project_data.pop('skills_ids', [])
            project_id = project_data.get('id', None)
            if project_id:
                project = Project.objects.get(id=project_id, profile=instance)
                for key, value in project_data.items():
                    setattr(project, key, value)
                project.skills.set(skills_ids)
                project.save()
            else:
                project = Project.objects.create(profile=instance, **project_data)
                project.skills.set(skills_ids)

        return instance
