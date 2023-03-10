"""SearchTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from contents import views as contentViews
from actions import views as actionsViews

#from django.conf.urls.static import static
#from django.conf import settings

admin.site.site_header = 'SearchTech Administration Portal'

urlpatterns = [
    path('', contentViews.index, name='index'),
    path('<int:num_page>/', contentViews.index, name='index'),
    path('project/<int:id>/', contentViews.detailed_content, name='detailed_content'),
    path('', contentViews.search_projects, name='search_projects'),
    path('drive/', contentViews.drive, name='drive'),
    path('drive/display/<int:id>', contentViews.drive_display, name='drive_display'),


    path('actions/fav/change/', actionsViews.fav_change, name='fav_change'),
    path('actions/like/change/', actionsViews.like_change, name='like_change'),
    path('actions/share/add/', actionsViews.share, name='share'),
    path('actions/comment/add/', actionsViews.comment_add, name='comment_add'),
		
    path("accounts/", include("django.contrib.auth.urls")),
		path("logout/", contentViews.logout_view, name="logout_view"),
		path("register/", contentViews.register.as_view(), name="register"),
    path('admin/', admin.site.urls),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)