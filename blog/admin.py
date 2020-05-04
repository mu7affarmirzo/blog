from django.contrib import admin
from .models import PostModel, CommentModel

# admin.site.register(PostModel)

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','status')
	list_filter = ('status','created','publish','author')
	search_fields = ('title','body')
	prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ('status','publish')

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','email','post','created','active')
	list_filter = ('active','created','updated')
	search_fields = ('name','email','body')