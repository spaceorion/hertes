from django.contrib import admin
from .models import product,Category,about_us,all_about_us,vision_mission, \
Our_purpose,Our_value,Our_progress,history,Slidingimage,Slidingimagebrand,\
Sub_category,Brand
# Register your models here.
admin.site.register(about_us)
admin.site.register(Brand)
admin.site.register(history)
admin.site.register(all_about_us)
admin.site.register(product)
admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(vision_mission)
admin.site.register(Our_purpose)
admin.site.register(Our_value)
admin.site.register(Our_progress)
admin.site.register(Slidingimage)
admin.site.register(Slidingimagebrand)

