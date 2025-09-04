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
    education = """Bachelor of Technology (B.Tech) in Computer Science & Engineering - 
R.R. Institute of Modern Technology, Lucknow | 2025 | CGPA: 7.9/10
Higher Secondary (12th Grade) – Bal Nikunj Inter College, 2021 (86%)
Secondary (10th Grade) – Bal Nikunj Inter College, 2019 (81%)"""

    summary=(
        "I’m a Full-Stack Developer with experience building real-world projects like a Voting Management System, Library Management System. I work with technologies such as Python & Django, PHP (Laravel), JavaScript, React, and SQL databases, and enjoy creating applications that are both efficient and user-friendly. From designing responsive UIs to building secure APIs and handling database logic, I take ownership of the full development cycle. I’ve also integrated features like live charts, authentication, dark/light themes, and PDF/Excel exports in my projects. I enjoy problem-solving, experimenting with new tools, and continuously improving my skills to deliver impactful solutions."
    ),
    links={"github": "https://github.com/KrishnaShuklaDeveloper", "linkedin": "https://www.linkedin.com/in/krishna-shukla-1b8834241/"}
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
    links={"gitHub": "https://github.com/KrishnaShuklaDeveloper/Digital-Library-Management-System"},
)
project1.skills.add(python, django, html)

project2 = Project.objects.create(
    profile=profile,
    title="Admin-Controlled Voting System",
    description="Secure voting system built with Django",
    links={"gitHub": "https://github.com/KrishnaShuklaDeveloper/Admin-Controlled-Voting-System"},
)
project2.skills.add(django, javascript, html)

project3 = Project.objects.create(
    profile=profile,
    title="FitLife and Wellness Information Portal",
    description="Health & fitness portal with full-stack features",
    links={"gitHub": "https://github.com/KrishnaShuklaDeveloper/FitLife-and-Wellness-Information-Portal/tree/main/Health%20and%20fitness"},
)
project3.skills.add(python, django, javascript, css)

print("✅ Seeding complete: Profile, Projects, Skills added!")



