import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from api.models import Profile, Skill, Project

Profile.objects.all().delete()
Skill.objects.all().delete()
Project.objects.all().delete()

p = Profile.objects.create(
    name="Krishna Shukla",
    email="krishnashukla9219448687@gmail.com",
    education="BTech CSE (Final Year)",
    summary="Python/Django developer — digital library, REST APIs",
    links={"github":"https://github.com/your-username","linkedin":"https://linkedin.com/in/your-handle","portfolio":"https://your-portfolio.site"}
)

s_python = Skill.objects.create(name="Python", level=5)
s_django = Skill.objects.create(name="Django", level=4)
s_js = Skill.objects.create(name="JavaScript", level=3)
s_html = Skill.objects.create(name="HTML", level=4)

proj1 = Project.objects.create(profile=p, title="Digital Library Management System", description="Django app: issue/return books, members, fines", links={"repo":"https://github.com/your-username/digital-library"})
proj1.skills.set([s_python, s_django])

proj2 = Project.objects.create(profile=p, title="Portfolio Site", description="Static responsive site", links={"repo":"https://github.com/your-username/portfolio","live":"https://your-portfolio.site"})
proj2.skills.set([s_html, s_js])

print("Seed complete")

