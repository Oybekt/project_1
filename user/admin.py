from django.contrib import admin
from .models import User, Follow


admin.site.register([User, Follow])



