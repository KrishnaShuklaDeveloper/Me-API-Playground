from api.models import Profile, Project, Skill

def run():
    # Clear old data
    Profile.objects.all().delete()
    Project.objects.all().delete()
    Skill.objects.all().delete()

    # Profile
    profile = Profile.objects.create(
        name="Krishna Shukla",
        email="krishnashukla9219448687@gmail.com",
        education="Bachelor of Technology (B.Tech) in Computer Science & Engineering R.R. Institute of Modern Technology, Lucknow | 2025 | CGPA: 7.9/10\nHigher Secondary (12th Grade) – Bal Nikunj Inter College, 2021 (86%)\nSecondary (10th Grade) – Bal Nikunj Inter College, 2019 (81%)",
        summary="I’m a Full-Stack Developer with experience building real-world projects like a Voting Management System, Library Management System..."
    )

    p1 = Project.objects.create(
        profile=profile,
        title="Digital Library Management System",
        description="Library management system using Django",
        link="https://github.com/yourrepo/library"
    )
    p1.skills.add(Skill.objects.create(name="Python", rating=5))
    p1.skills.add(Skill.objects.create(name="Django", rating=4))
    p1.skills.add(Skill.objects.create(name="HTML", rating=5))

    p2 = Project.objects.create(
        profile=profile,
        title="Admin-Controlled Voting System",
        description="Secure voting system built with Django",
        link="https://github.com/yourrepo/voting"
    )
    p2.skills.add(Skill.objects.create(name="Django", rating=4))
    p2.skills.add(Skill.objects.create(name="JavaScript", rating=3))
    p2.skills.add(Skill.objects.create(name="HTML", rating=5))

    p3 = Project.objects.create(
        profile=profile,
        title="FitLife and Wellness Information Portal",
        description="Health & fitness portal with full-stack features",
        link="https://github.com/yourrepo/fitlife"
    )
    p3.skills.add(Skill.objects.create(name="Python", rating=5))
    p3.skills.add(Skill.objects.create(name="Django", rating=4))
    p3.skills.add(Skill.objects.create(name="JavaScript", rating=3))
    p3.skills.add(Skill.objects.create(name="CSS", rating=4))

    Skill.objects.create(name="Python", rating=5, profile=profile)
    Skill.objects.create(name="HTML", rating=5, profile=profile)
    Skill.objects.create(name="Django", rating=4, profile=profile)
    Skill.objects.create(name="CSS", rating=4, profile=profile)
    Skill.objects.create(name="SQL", rating=4, profile=profile)
    Skill.objects.create(name="JavaScript", rating=3, profile=profile)
    Skill.objects.create(name="PHP", rating=3, profile=profile)
    Skill.objects.create(name="Laravel", rating=3, profile=profile)
