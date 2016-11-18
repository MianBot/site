from django.contrib import admin

from .models import Post
from .models import IDForm
from .models import LogForm

admin.site.register(Post)
admin.site.register(IDForm)
admin.site.register(LogForm)
