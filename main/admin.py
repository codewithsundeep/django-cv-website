from django.contrib import admin
from main.models import personal_info,Skills,Languages,Current_Work,Work_Experience,Education,Social_Links,contact


# Register your models here.
admin.site.register(personal_info)
admin.site.register(Languages)
admin.site.register(Skills)
admin.site.register(Current_Work)
admin.site.register(Work_Experience)
admin.site.register(Education)
admin.site.register(Social_Links)
admin.site.register(contact)
