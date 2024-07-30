from django.contrib import admin
from .models import List, ListItem, Category


admin.site.register(List)
admin.site.register(ListItem)
admin.site.register(Category)
