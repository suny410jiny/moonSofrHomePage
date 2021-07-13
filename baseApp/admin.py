from django.contrib import admin
from .models import Post, Tag, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','title','author', 'caption','postDivision']
    list_display_links = ['title']
    search_fields = ['postDivision']
    list_filter = ['postDivision']
    fields = ['title','tag', 'postDivision', 'caption','tag_set','thumnail','body',]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


