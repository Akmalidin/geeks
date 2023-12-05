from django.contrib import admin
from .models import Settings, About, AboutMe, AboutMeSkills, Services, Happy_Clients, Portfolio, Reviews, Contact
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'logo')
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'desc')
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'image')
@admin.register(AboutMeSkills)
class AboutMeSkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'suptitle')
@admin.register(Happy_Clients)
class Happy_ClientsAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('category', 'image')
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'image')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')