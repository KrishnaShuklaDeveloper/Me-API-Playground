**Me-API Playground**



A Django REST API playground for experimenting with user profiles, API testing, and search functionality.

This project is built using Django, Django REST Framework.



**Architecture**



**Backend**: Django 5.2, Django REST Framework

**Database**: SQLite (default, easy for local testing)

**Static Files**: Served using Whitenoise

**Deployment Ready**: Procfile, runtime.txt, requirements.txt included



**Project Hosted on Render** 

**To see output** - https://me-api-playground-kn58.onrender.com/

**To check API's**

**Health Check**- https://me-api-playground-kn58.onrender.com/api/health/

**Profiles**- https://me-api-playground-kn58.onrender.com/api/profiles/

**Projects**- https://me-api-playground-kn58.onrender.com/api/projects/

**Skills**- https://me-api-playground-kn58.onrender.com/api/skills/


**Setup**



**Local Setup:**



**Clone the repository:**

git clone https://github.com/KrishnaShuklaDeveloper/Me-API-Playground.git

**Actual repo link** - https://github.com/KrishnaShuklaDeveloper/Me-API-Playground

cd Me-API-Playground



**Create and activate a virtual environment:**

python -m venv .venv

source .venv/bin/activate (Linux/Mac)

.venv\\Scripts\\activate (Windows)



**Install dependencies:**

pip install -r requirements.txt



**Run migrations:**

python manage.py migrate



**Seed sample data:**

python seed\_me.py



**Start the development server:**

python manage.py runserver



Your API will be available at http://127.0.0.1:8000/



**Production Setup:**



Use Gunicorn as the app server:

web: gunicorn config.wsgi





**Database Schema**



**Profiles Table**:



id (AutoField, Primary Key)

name (CharField)

email (EmailField, unique)

bio (TextField, optional)



**Working URLs**



**API Root**: http://127.0.0.1:8000/api/



**Profiles List \& Create**: http://127.0.0.1:8000/api/profiles/



**Single Profile** (example with ID=1): http://127.0.0.1:8000/api/profiles/1/



**Search Profiles**: http://127.0.0.1:8000/api/profiles/?search=krishna



**Admin Panel**: http://127.0.0.1:8000/admin/



**Health Check**: http://127.0.0.1:8000/api/health/


## Superuser Access (Local Setup)

To access the Django admin panel, create your own superuser after setting up the project:

```bash
python manage.py createsuperuser




**Sample Usage with cURL**



**Create Profile:**

curl -X POST http://127.0.0.1:8000/api/profiles/

&nbsp;-H "Content-Type: application/json" -d '{"name": "John", "email": "john@gmail.com

", "bio": "Hi from cURL"}'



**Search Profile:**

curl http://127.0.0.1:8000/api/profiles/?search=john



**Author**



Hi, I’m Krishna Shukla



**Resume**: https://drive.google.com/file/d/1aUYGpc-z3cEOdFgxm91TMZjRy7YLQnIa/view?usp=sharing



**LinkedIn**: https://www.linkedin.com/in/krishna-shukla-1b8834241/



**GitHub**: https://github.com/KrishnaShuklaDeveloper





