from django.contrib import admin
from  app.models import CustomUserModel, Article

# Register your models here.

admin.site.register(CustomUserModel)
admin.site.register(Article)