# Create your views here.
from assault_app.models import Schools, Comment, CommentForm
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
import string

def school(request, pk):
    school = get_object_or_404(Schools, id=pk)
    school.content_split = school.content.replace('[','').replace(']','').replace('</div>, <div','</div> <div')
    comments = Comment.objects.filter(school=school)
    if request.method == 'POST':
        form = CommentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            body = form.cleaned_data['comment']
            form.save()
            #content = Comment.objects.create(school = school, author = "Anonomyous Author", body = comment)
            #new_comment = Comment.objects.get(pk=1)
            form = CommentForm(instance=new_comment)
            form.save()
    else:
        form = CommentForm()

    school_list = Schools.objects.all()
    context = {
        'school': school,
        'comments': comments,
        'form': form,
#       'user': user,
        'schools': school_list,
    }
    return render(request, "assault_app/school.html", context)
    #return render_to_response("assault_app/school.html", d)
    

def all_schools(request):
    school_list = Schools.objects.all()
    paginator = Paginator(school_list, 50)
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

def resources(request):
    school_list = Schools.objects.all()
    context = {
        'school': school,
        'schools': school_list,
    }
    return render(request, "assault_app/resources.html", context)

def about(request):
    school_list = Schools.objects.all()
    context = {
        'school': school,
        'schools': school_list,
    }
    return render(request, "assault_app/about.html", context)



