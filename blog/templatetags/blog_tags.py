from django import template
from ..models import PostModel
from django.db.models import Count

register = template.Library()

@register.simple_tag
def get_most_commented_posts(count=5):
	return PostModel.published.annotate(
		total_comments=Count('comments')
		).order_by('-total_comments')[:count]

@register.simple_tag
def total_posts():
	return PostModel.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = PostModel.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}