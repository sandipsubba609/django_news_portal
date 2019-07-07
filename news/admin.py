from django.contrib import admin
from news.models import News
# Register your models here.

# admin.site.register(News)

@admin.register(News)
class newsadmin(admin.ModelAdmin):
    list_display=('title','created_at')
    list_filter=('category',)