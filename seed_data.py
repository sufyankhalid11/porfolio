import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from Base.models import Skill, Experience, Project, UserProfile

def run_seeder():
    print("Seeding portfolio data...")

    # 1. Skills added in your stack
    skills = [
        {'name': 'Python', 'category': 'language', 'proficiency_icon': 'fab fa-python'},
        {'name': 'C++', 'category': 'language', 'proficiency_icon': 'fas fa-code'},
        {'name': 'JS', 'category': 'language', 'proficiency_icon': 'c'},
        {'name': 'DJANGO', 'category': 'backend', 'proficiency_icon': 'fas fa-server'},
        {'name': 'PostgreSQL', 'category': 'database', 'proficiency_icon': 'fas fa-database'},
    ]
    for s in skills:
        Skill.objects.get_or_create(name=s['name'], defaults={'category': s['category'], 'proficiency_icon': s['proficiency_icon']})
    print("-> Skills added successfully!")

    # 2. Experience & Education items
    experiences = [
        {
            'title': 'Backend .NET Developer',
            'organization': 'Dunify',
            'duration': '1 Year',
            'description': 'Developed and maintained robust backend services and APIs.',
            'category': 'work'
        },
        {
            'title': 'Founder & Data Consultant',
            'organization': 'Data Insights',
            'duration': '2026 - Present',
            'description': 'Building automated data intelligence solutions and outreach tools.',
            'category': 'work'
        },
        {
            'title': 'Bachelor of Data Science',
            'organization': 'FAST NUCES Lahore',
            'duration': '2024 - Present',
            'description': 'Studying data science, low-level architecture, and web systems.',
            'category': 'education'
        }
    ]
    for exp in experiences:
        Experience.objects.get_or_create(
            title=exp['title'],
            organization=exp['organization'],
            defaults={'duration': exp['duration'], 'description': exp['description'], 'category': exp['category']}
        )
    print("-> Experiences added successfully!")

    # 3. Featured Projects
    projects = [
        {
            'title': 'Hospital Management System',
            'description': 'A custom console-based Hospital CRM system with SFML UI',
            'technology': 'Python, Google OAuth',
            'project_url': 'https://github.com/sufyankhalid11'
        },
        {
            'title': 'Console Candy Crush Game',
            'description': 'A custom console-based game featuring modular matrix manipulation, grid boundary checks, and cascading gravity logic in C++.',
            'technology': 'C++',
            'project_url': 'https://github.com/sufyankhalid11'
        }
    ]
    for proj in projects:
        Project.objects.get_or_create(
            title=proj['title'],
            defaults={'description': proj['description'], 'technology': proj['technology'], 'project_url': proj['project_url']}
        )
    print("-> Projects added successfully!")
    print("Portfolio database seeding complete!")

if __name__ == '__main__':
    run_seeder()