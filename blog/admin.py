from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    # prepulated_fields = {'slug': ('title',)}
