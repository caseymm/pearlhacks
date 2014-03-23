# Create your views here.
from assault_app.models import Schools#, SchoolStoryFeed
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import string

def school(request, pk):
    school = get_object_or_404(Schools, id=pk)

    context = {
        'school': school,
    }
    return render(request, "assault_app/school.html", context)
    

def all_schools(request):
    school_list = Schools.objects.all()
    paginator = Paginator(school_list, 25)
    page = request.GET.get('page')
    try:
        schools = paginator.page(page)
    except PageNotAnInteger:
         #If page is not an integer, deliver first page
        schools = paginator.page(1)
        
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page of results
        schools = paginator.page(paginator.num_pages)

    
    context = {
        'schools': schools,
    }
    
    return render(request, 'assault_app/all_schools.html', context)

def resources(request, pk):
    context = {
        
    }
    return render(request, "assault_app/resources.html", context)

def about(request, pk):
    context = {
        
    }
    return render(request, "assault_app/about.html", context)



