from django.contrib import admin

# Register your models here.
from tasks.models import To_do_Model

admin.site.register(To_do_Model)