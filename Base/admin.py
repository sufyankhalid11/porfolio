from django.contrib import admin
from .models import Project, ProjectImage, UserProfile, ContactMessage, Skill, Experience

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

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