from django.contrib import admin
from .models import Post, Category, Comment, UserProfile
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "created_date", "active", "comment")
    list_filter = ("active", "created_date")
    search_fields = ("email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, queryset):
        queryset.update(active=True)
