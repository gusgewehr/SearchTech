from django.contrib import admin
from .models import Comment, Favorite, Like, Share

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['user',
		'content',
		'allowed',
		'text',
		'created'
    ]

admin.site.register(Comment, CommentAdmin)
class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite
    list_display = ['user',
		'content',
		'created'
    ]
admin.site.register(Favorite, FavoriteAdmin)

class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ['user',
		'content',
		'created'
    ]
admin.site.register(Like, LikeAdmin)

class ShareAdmin(admin.ModelAdmin):
    model = Share
    list_display = ['user',
		'content',
		'created'
    ]
admin.site.register(Share, ShareAdmin)