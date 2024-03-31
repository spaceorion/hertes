from django.shortcuts import render
from .models import about_us,all_about_us,Our_progress,Our_purpose,Our_value,vision_mission,history
# Create your views here.
def index(request):
    return render(request,'index.html')
#
def about(request):
    about_obj = about_us.objects.all()
    return render(request,'about_us/about_us.html',{'about':about_obj})
#
def our_value(request):
    value_obj = Our_value.objects.all()
    return render(request,'about_us/about_us.html',{'about':value_obj})
#
def our_progress(request):
    about_obj = Our_progress.objects.all()
    return render(request,'about_us/our_purpose.html',{'about':about_obj})
#
def vission_and_mission(request):
    about_obj = vision_mission.objects.all()
    return render(request,'about_us/vision_&_mission.html',{'about':about_obj})
#
def our_purpose(request):
    about_obj = Our_purpose.objects.all()
    return render(request,'about_us/our_purpose.html',{'about':about_obj})
#
def our_history(request):
    history_obj = history.objects.all()
    return render(request,'history.html',{'about':history_obj})

#
def all_about(request):
    about_obj = all_about_us.objects.all()
    return render(request,'about_us/all_about_us.html',{'about':about_obj})
#
def contect_us(request):
    return render(request,'conteck_us.html')