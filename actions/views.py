from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import requests

from .models import Favorite, Like, Comment, Share

# Create your views here.
@login_required
def fav_change(request):
    if request.method == 'POST':
        requestUser = request.user
        requestContent = request.POST['projectId']
        if request.POST['fav_btn'] == 'add':
            fav = Favorite(
                user = requestUser,
                content = requestContent
            )
            fav.save()
        elif request.POST['fav_btn'] == 'remove':
            fav = Favorite.objects.get(user=requestUser, content=requestContent)
            fav.delete()
    
    return redirect('/project/'+requestContent)

@login_required
def like_change(request):
    if request.method == 'POST':
        requestUser = request.user
        requestContent = request.POST['projectId']
        if request.POST['like_btn'] == 'add':
            like = Like(
                user = requestUser,
                content = requestContent
            )
            like.save()
        elif request.POST['like_btn'] == 'remove':
            like = Like.objects.get(user=requestUser, content=requestContent)
            like.delete()
    
    return redirect('/project/'+requestContent)

@login_required
def share(request):
    if request.method == 'POST':
        requestUser = request.user
        requestContent = request.POST['projectId']
        share = Share(
            user = requestUser,
            content = requestContent
            )
        share.save()
    
    return redirect(f'/project/{requestContent}/?showShare=1')

@login_required()
def comment_add(request):
    if request.method == 'POST':
        requestUser = request.user
        requestContent =  request.POST['projectId']
        requestComment = request.POST['comment']

        comment = Comment(
            user = requestUser,
            content = requestContent,
            text = requestComment,
            allowed = True
        )
        if requestComment and requestContent and requestUser:
            comment.save()    
    
            return redirect('/project/'+requestContent)
        else:
            return redirect(f'/project/{requestContent}/?error_message=obligatory_text')
    
