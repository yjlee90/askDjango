from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin) :

    list_display =['id', 'title', 'content_size', 'status', 'content']
    actions = ['make_published', 'make_draft', 'make_withdrawn']

    def content_size(self, post):
            return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '내용 글자수'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{} 건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다.'

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w')
        self.message_user(request, '{} 건의 포스팅을 Warningithdrawn상태로 변경'.format(updated_count))
    make_withdrawn.short_description = '지정 포스팅을 Warningithdrawn상태로 변경합니다.'


    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} 건의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Publsiehd상태로 변경합니다.'
