import os
from django.db import models

# from cloudinary_storage.storage import MediaCloudinaryStorage

# class RawMediaCloudinaryStorage(MediaCloudinaryStorage):
#     def _get_resource_type(self, *args, **kwargs):
#         return "auto"

class UserProfile(models.Model):
    name = models.CharField(max_length=100, default="Muhammad Sufyan Khalid")
    title = models.CharField(max_length=200, default="Data Science Student & Full-Stack Developer")
    bio = models.TextField(default="Passionate backend and full-stack developer specializing in building scalable web applications.")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    
    # resume = models.FileField(upload_to='resumes/', storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = UserProfile.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.profile_image and old_instance.profile_image != self.profile_image:
                if os.path.isfile(old_instance.profile_image.path):
                    os.remove(old_instance.profile_image.path)
        super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Project.objects.filter(pk=self.pk).first()
            if old_instance and old_instance.image and old_instance.image != self.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery/')

    def __str__(self):
        return f"Image for {self.project.title}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Languages'),
        ('backend', 'Backend & Frameworks'),
        ('database', 'Databases'),
        ('tool', 'Tools & Platforms'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='language')
    proficiency_icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"  


class Experience(models.Model):
    CHOICES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
    ]
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CHOICES, default='work')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.organization}"