from django.contrib import admin

# Register your models here.
from .models import Article

# We can do this more user-friendly
# so what will happen it will make your admin page more verbose and user friendly
class ArticleAdmin(admin.ModelAdmin):
    # this is more roboust way to display model contents to the admin dashboard.
    list_display = ["id","title"]
    search_fields = ["title","content"] # so this will make your search box
    

# registering your model with admin
admin.site.register(Article, ArticleAdmin) # so you can also register your own class with requirement specific functionalities.