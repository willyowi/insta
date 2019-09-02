from django.contrib import admin
from .models import Post,tags


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

#admin.site.register(Editor)
admin.site.register(Post,PostAdmin)
admin.site.register(tags
)
