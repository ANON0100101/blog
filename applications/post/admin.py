from django.contrib import admin
from applications.post.models import Post,Comment


admin.site.register(Post)
admin.site.register(Comment)