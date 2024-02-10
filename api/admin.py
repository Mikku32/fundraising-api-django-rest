from django.contrib import admin

from api.models import Donation,  Project, User

# Register your models here.

@admin.register(User)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Donation)
class ProjectAdmin(admin.ModelAdmin):
    pass


