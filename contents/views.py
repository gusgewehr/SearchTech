from functools import lru_cache
from math import ceil
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from datetime import date
import requests
from actions.models import Favorite, Like, Comment, Share
from .models import Drive
from django.http import HttpResponse
import os

# Create your views here
@lru_cache(maxsize=30)
def get_all_project(date):
    url =  'https://api.nasa.gov/techport/api/projects?api_key=jEsssS4hRlXHUKj6uLRArcZG2LOITXr8YKWc00e6'
    response = requests.get(url)
    print(response.headers['X-RateLimit-Remaining'])
    resp_dict = response.json()
    return resp_dict['projects']

@lru_cache()
def get_specific_project(id, month):
    url = f'https://techport.nasa.gov/api/projects/search?projectId={id}&api_key=jEsssS4hRlXHUKj6uLRArcZG2LOITXr8YKWc00e6'
    response = requests.get(url)
    resp_dict = response.json()
    return resp_dict['projects']

@lru_cache()
def get_datailed_project(id, month):
    url = f'https://techport.nasa.gov/api/projects/{id}?api_key=jEsssS4hRlXHUKj6uLRArcZG2LOITXr8YKWc00e6'
    response = requests.get(url)
    #print(response.headers['X-RateLimit-Remaining'])
    resp_dict = response.json()
    return resp_dict['project']

@lru_cache
def search_projects(query, date):
	url = f'https://techport.nasa.gov/api/projects/search?searchQuery={query}'
	response = requests.get(url)
	resp_dict = response.json()

	return resp_dict['projects']

def login(request):
    ''' Recebe as solicitações de login, se não tiver autenticado retorna com a tela de login'''
    if request.user.is_authenticated:
        redirect('/')
    else:
        return render(request, 'login.html')

def logout_view(request):
    ''' Recebe as solicitações de logout, redireciona pro endereço raiz.'''
    logout(request)
    return redirect('/')

def index(request, num_page = 1):
	try:
		query = request.GET['querySearch']
	except:
		query = None

	if query:		
		response = search_projects(query, date.today())
	else:
		response = get_all_project(date.today())

	total_pages = ceil(len(response)/5)

	page = response[((num_page*5)-5):(num_page*5)]

	contents = []
	for item in page:
		project = get_specific_project(item['projectId'], date.today().month)
		contents.append(project[0])

	context = { 
			'contents': contents, 
			'total_pages': total_pages, 
			'num_page':num_page,
			'next_page':num_page+1,
			'prev_page':num_page-1,
	}

	return render(request, 'index.html',context)

@login_required()
def detailed_content(request, id):
    user = request.user

    project = get_datailed_project(id, date.today().month)

    
    favBool = Favorite.objects.filter(user=user, content=id)
    likeBool = Like.objects.filter(user=user, content=id)
    comments = Comment.objects.filter(content=id, allowed=True)


    context = {
        'project': project,
        'userFav': favBool,
        'userLike': likeBool,
        'comments': comments,
        }

    return render(
        request,
        'datailed.html',
        context
    )

class register(generic.CreateView):
	form_class = UserCreationForm
	template_name ='registration/register.html'	

	def form_valid(self, form):
		context = self.get_context_data(form=form)
		context['success'] = True
		teste = self.request.GET['next']
		form.save()
		return redirect(f'/accounts/login/?next={teste}')

@login_required
def drive(request):
    files = Drive.objects.all()

    context = {
        'files': files,
    }

    return render(request, 'drive.html',context)


@login_required
def drive_display(request,id):
    file = Drive.objects.get(id=id)

    response = HttpResponse()
    caminho, file_name = os.path.split(file.file.path)

    if file_name.endswith('.mp3'):
        content_type = 'audio/mp3'
    elif file_name.endswith('.png'):
        content_type = 'image/png'
    elif file_name.endswith('.mp4'):
        content_type = 'video/mp4'

    response = HttpResponse(file.file, headers={
        'Content-Type': content_type,
        'Content-Disposition': f'attatchment; filename="{file_name}"'
    })

    return response 
    