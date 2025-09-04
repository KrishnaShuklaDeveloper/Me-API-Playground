import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from api.models import Profile, Project, Skill

Profile.objects.all().delete()
Project.objects.all().delete()
Skill.objects.all().delete()

profile = Profile.objects.create(
    name="Krishna Shukla",
    email="krishnashukla9219448687@gmail.com",
    education=(
        "Bachelor of Technology (B.Tech) in Computer Science & Engineering\n"
        "R.R. Institute of Modern Technology, Lucknow | 2025 | CGPA: 7.9/10\n"
        "Higher Secondary (12th Grade) – Bal Nikunj Inter College, 2021 (86%)\n"
        "Secondary (10th Grade) – Bal Nikunj Inter College, 2019 (81%)"
    ),
    summary=(
        "I’m a Full-Stack Developer with experience building real-world projects "
        "like a Voting Management System, Library Management System. I work with "
        "technologies such as Python & Django, PHP (Laravel), JavaScript, React, "
        "and SQL databases, and enjoy creating applications that are both efficient "
        "and user-friendly. From designing responsive UIs to building secure APIs "
        "and handling database logic, I take ownership of the full development cycle. "
        "I’ve also integrated features like live charts, authentication, dark/light "
        "themes, and PDF/Excel exports in my projects. I enjoy problem-solving, "
        "experimenting with new tools, and continuously improving my skills to "
        "deliver impactful solutions."
    ),
    links="GitHub | LinkedIn"
)

Project.objects.create(
    profile=profile,
    title="Digital Library Management System",
    description="Library management system using Django",
    link="https://github.com/KrishnaShuklaDeveloper/Digital-Library",
    skills="Python (5/5), Django (4/5), HTML (5/5)"
)

Project.objects.create(
    profile=profile,
    title="Admin-Controlled Voting System",
    description="Secure voting system built with Django",
    link="https://github.com/KrishnaShuklaDeveloper/Voting-System",
    skills="Django (4/5), JavaScript (3/5), HTML (5/5)"
)

Project.objects.create(
    profile=profile,
    title="FitLife and Wellness Information Portal",
    description="Health & fitness portal with full-stack features",
    link="https://github.com/KrishnaShuklaDeveloper/FitLife-Portal",
    skills="Python (5/5), Django (4/5), JavaScript (3/5), CSS (4/5)"
)

Skill.objects.create(profile=profile, name="Python", rating=5)
Skill.objects.create(profile=profile, name="HTML", rating=5)
Skill.objects.create(profile=profile, name="Django", rating=4)
Skill.objects.create(profile=profile, name="CSS", rating=4)
Skill.objects.create(profile=profile, name="SQL", rating=4)
Skill.objects.create(profile=profile, name="JavaScript", rating=3)
Skill.objects.create(profile=profile, name="PHP", rating=3)
Skill.objects.create(profile=profile, name="Laravel", rating=3)

print("✅ Seed data inserted successfully")
