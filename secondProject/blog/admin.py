from django.contrib import admin

# Register your models here.
from .models import Post, category
admin.site.register(Post)
admin.site.register(category)