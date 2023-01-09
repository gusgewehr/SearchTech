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

urlpatterns = [
    path('', contentViews.index, name='index'),
    path('<int:num_page>/', contentViews.index, name='index'),
    path('project/<int:id>/', contentViews.detailed_content, name='detailed_content'),
    path('actions/fav/change/', actionsViews.fav_change, name='fav_change'),
    path('actions/like/change/', actionsViews.like_change, name='like_change'),
    path('actions/share/add/', actionsViews.share, name='share'),
    path('actions/comment/add/', actionsViews.comment_add, name='comment_add'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)