# Create your views here.
from assault_app.models import Schools, Comment, CommentForm
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
import string

def school(request, pk):
    school = get_object_or_404(Schools, id=pk)
    school.content_split = school.content.replace('[','').replace(']','').replace('</div>, <div','</div> <div').replace('</article>, <article','</article> <article')
    comments = Comment.objects.filter(school=school)
    school_list = Schools.objects.all()[:50]
    context = {
        'school': school,
        'comments': comments,
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


def add_comment(request):
    school_list = Schools.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            school = form.cleaned_data['school']
            form.save()
            #comment = Comment.objects.create(school = school, author = author, body = body)
            return HttpResponseRedirect('/')
        #return render(request, 'assault_app/add_comment.html', context)
    form = CommentForm()
    context = {
            'form': form,
            #'school': school,
            'schools': school_list,
            }

    return render(request, "assault_app/add_comment.html", context)

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



