from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        for post in queryset:
            post.publish()
    publish_posts.short_description = "Publish selected posts"

admin.site.register(Post, PostAdmin)
