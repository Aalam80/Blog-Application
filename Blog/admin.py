from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Group
from django.utils.html import format_html

admin.site.site_header ='Blog admin Panel'
admin.site.site_title='custom Admin pnel'
# Register your models here.

class CustomAdminPost(admin.ModelAdmin):
    list_display= ('author_name','len_content')
    list_filter=('author_name','title')
    search_fields=('author_name',)
    list_per_page = 2
    list_display_links=('author_name','len_content')
    save_on_top= True


    def len_content(self,obj):
        return format_html(f'<span style="color:green;" >{obj.content[:20] } </span>')
        # return obj.content[:20]

admin.site.register(Post,CustomAdminPost)
#unregister your model:
admin.site.unregister(Group)