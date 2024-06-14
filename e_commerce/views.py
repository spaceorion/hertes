from django.shortcuts import render
from .models import about_us,all_about_us,Our_progress,Our_purpose,Our_value,vision_mission,history,\
Slidingimage,Slidingimagebrand,product,Category,Brand
# Create your views here.

def index(request):
    slid_obj=Slidingimage.objects.all()
    slid_obj_brand=Slidingimagebrand.objects.all()
    category= Category.objects.all()
    brand_obj=Brand.objects.all()
    CategoryId = request.GET.get('category')
    if CategoryId:
        product_obj = product.objects.filter(sub_category=CategoryId).order_by('-id')
    else:
        product_obj=product.objects.all()
    context={
        'product':product_obj,
        'category':category,
        'brand':brand_obj,
        'first_slid':slid_obj,
        'slid_second':slid_obj_brand,
    }
    return render(request,'kk.html',context)
#
def product_list(request, subcategory_id):
    products = product.objects.filter(sub_category=subcategory_id)
    slid_obj_brand=Slidingimagebrand.objects.all()
    slid_obj=Slidingimage.objects.all()
    context={
        "products":products,
        "slid_second":slid_obj_brand,
        'first_slid':slid_obj,

    }
    return render(request, 'product_list.html',context)
#
#
#
def about(request):
    about_obj = about_us.objects.all()
    return render(request,'about_us/about_us.html',{'about':about_obj})
#
def our_value(request):
    slid_obj_brand=Slidingimagebrand.objects.all()
    value_obj = Our_value.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
        'about':value_obj,
    }
    return render(request,'about_us/our_values.html',context)
#
def our_progress(request):
    slid_obj_brand=Slidingimagebrand.objects.all()
    about_obj = Our_progress.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
        'about':about_obj,
    }
    return render(request,'about_us/our_purpose.html',context)
#
def vission_and_mission(request):
    slid_obj_brand=Slidingimagebrand.objects.all()
    about_obj = vision_mission.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
        'about':about_obj
    }
    return render(request,'about_us/vision_&_mission.html',context)
#
def our_purpose(request):
    slid_obj_brand=Slidingimagebrand.objects.all()
    about_obj = Our_purpose.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
        'about':about_obj,
    }
    return render(request,'about_us/our_purpose.html',context)
#
def our_history(request):
    slid_obj_brand=Slidingimagebrand.objects.all()
    history_obj = history.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
        'about':history_obj,
    }
    return render(request,'history.html',context)

#
def all_about(request):
    slid_obj_brand=Slidingimagebrand.objects.all()
    about_obj = all_about_us.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
        'about':about_obj,
    }
    return render(request,'about_us/all_about_us.html',context)
#
def contect_us(request):
    slid_obj_brand=Slidingimagebrand.objects.all()

    context={
       
        'slid_second':slid_obj_brand,
    }
    return render(request,'conteck_us.html')
#
