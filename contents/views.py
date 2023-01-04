from functools import lru_cache
from math import ceil
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
import requests

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
    return resp_dict




def index(request, num_page = 1):
    
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

    return render(
        request, 
        'index.html',
        context 
        )


@login_required()
def detailed_content(request, id):


    project = get_datailed_project(id, date.today().month)


    context = {
        'project': project,
        }

    return render(
        request,
        'datailed.html',
        context
    )
