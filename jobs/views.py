from django.shortcuts import render
from .models import Job, Bio, BioPic, BackgroundImage, Certifications, Education

def home(request):
    jobs = Job.objects.order_by('-start_date')
    bio = Bio.objects
    bio_pic = BioPic.objects
    background = BackgroundImage.objects
    certs = Certifications.objects
    education = Education.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'bio': bio,
                             'bio_pic': bio_pic, 'background': background, 
                             'certs': certs, 'education':education})
