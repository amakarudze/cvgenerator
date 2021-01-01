import io

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import pdfkit

from .models import Profile

# Create your views here.


def accept(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        summary = request.POST['summary']
        degree = request.POST['degree']
        school = request.POST['school']
        university = request.POST['university']
        previous_work = request.POST['previous_work']
        skills = request.POST['skills']

        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)
        profile.save()
    return render(request, 'pdf/accept.html')


def index(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/index.html', {'profiles': profiles})


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response
