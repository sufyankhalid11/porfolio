from django.contrib import admin
from .models import Project, ProjectImage, UserProfile, ContactMessage, Skill, Experience

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(UserProfile)
admin.site.register(ContactMessage)
admin.site.register(Skill)

admin.site.register(Experience)