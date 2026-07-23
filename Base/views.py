import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, UserProfile, ContactMessage, Skill, Experience

def get_github_stats(username="sufyankhalid11"):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        pass
    return None

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('home')

    projects = Project.objects.all().order_by('-created_at')
    profile = UserProfile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-created_at')
    github_data = get_github_stats("sufyankhalid11")
    
    context = {
        'projects': projects,
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'github_data': github_data,
    }
    return render(request, 'home.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})