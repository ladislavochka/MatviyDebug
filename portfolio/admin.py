from django.contrib import admin
from portfolio.models import Poll

admin.site.site_header = "My Portfolio Admin"
admin.site.register(Poll)
# Register your models here.
