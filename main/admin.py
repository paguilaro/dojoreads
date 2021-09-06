from django.contrib import admin
from .models import User, Authors, Books, Reviews

# Register your models here.
admin.site.register(User)
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Reviews)

