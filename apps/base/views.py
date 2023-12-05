from django.shortcuts import render, redirect
from .models import Settings, About, AboutMe, AboutMeSkills, Services, Happy_Clients, Portfolio, Reviews, Contact
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    about_me = AboutMe.objects.latest('id')
    about_me_skills = AboutMeSkills.objects.all()
    services = Services.objects.all()
    happy = Happy_Clients.objects.all()
    portfolio = Portfolio.objects.all()
    reviews = Reviews.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name = name, email = email, message = message)
        return redirect('index')
    return render(request, 'index.html', locals())