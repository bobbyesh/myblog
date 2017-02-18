from django.contrib import admin
from blogapp.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
