from django.shortcuts import render
from .models import Journal, Work, AboutMe, MainDetails

# Create your views here.
def index(request): 
    journals = Journal.objects.all().order_by('-published_date')
    works = Work.objects.all().order_by('-completion_date')
    aboutme = AboutMe.objects.first()
    maindetails = MainDetails.objects.first()
    return render(request, 'index.html', {'journals': journals, 'works': works, 'aboutme': aboutme, 'maindetails': maindetails})
