from django.contrib import admin
from .models import Journal, Work, AboutMe, MainDetails

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'image')
    search_fields = ('title', 'content')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'completion_date', 'image')
    search_fields = ('title', 'description')
    list_filter = ('completion_date',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['title', 'primary_caption', 'secondary_caption']
    search_fields = ['title' ,'primary_caption', 'secondary_caption']

@admin.register(MainDetails)
class MainDetailsAdmin(admin.ModelAdmin):
    list_display = ['main_heading', 'sub_heading', 'email', 'phone_no']
    search_fields = ['main_heading', 'sub_heading', 'email', 'phone_no']
