from django.contrib import admin
from blog.models import Post, Category
# don't add comments to admin 
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
