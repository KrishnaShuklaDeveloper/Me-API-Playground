import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from api.models import Profile, Project, Skill

# Clear old data
Profile.objects.all().delete()
Project.objects.all().delete()
Skill.objects.all().delete()

# Create Profile
profile = Profile.objects.create(
    name="Krishna Shukla",
    email="krishnashukla9219448687@gmail.com",
    education=(
        "Bachelor of Technology (B.Tech) in Computer Science & Engineering "
        "R.R. Institute of Modern Technology, Lucknow | 2025 | CGPA: 7.9/10\n"
        "Higher Secondary (12th Grade) – Bal Nikunj Inter College, 2021 (86%)\n"
        "Secondary (10th Grade) – Bal Nikunj Inter College, 2019 (81%)"
    ),
    summary=(
        "I’m a Full-Stack Developer with experience building real-world projects "
        "like a Voting Management System, Library Management System. I work with "
        "technologies such as Python & Django, PHP (Laravel), JavaScript, React, "
        "and SQL databases, and enjoy creating applications that are both efficient "
        "and user-friendly."
    ),
    links={
        "GitHub": "https://github.com/KrishnaShuklaDeveloper",
        "LinkedIn": "https://linkedin.com/in/krishnashukla",
    },
)

# Create Skills
python = Skill.objects.create(name="Python", level=5)
django = Skill.objects.create(name="Django", level=4)
html = Skill.objects.create(name="HTML", level=5)
css = Skill.objects.create(name="CSS", level=4)
sql = Skill.objects.create(name="SQL", level=4)
javascript = Skill.objects.create(name="JavaScript", level=3)
php = Skill.objects.create(name="PHP", level=3)
laravel = Skill.objects.create(name="Laravel", level=3)

# Create Projects
project1 = Project.objects.create(
    profile=profile,
    title="Digital Library Management System",
    description="Library management system using Django",
    links={"GitHub": "https://github.com/KrishnaShuklaDeveloper/Digital-Library-Management-System"},
)
project1.skills.add(python, django, html)

project2 = Project.objects.create(
    profile=profile,
    title="Admin-Controlled Voting System",
    description="Secure voting system built with Django",
    links={"GitHub": "https://github.com/KrishnaShuklaDeveloper/Voting-System"},
)
project2.skills.add(django, javascript, html)

project3 = Project.objects.create(
    profile=profile,
    title="FitLife and Wellness Information Portal",
    description="Health & fitness portal with full-stack features",
    links={"GitHub": "https://github.com/KrishnaShuklaDeveloper/FitLife-Portal"},
)
project3.skills.add(python, django, javascript, css)

print("✅ Seeding complete: Profile, Projects, Skills added!")
