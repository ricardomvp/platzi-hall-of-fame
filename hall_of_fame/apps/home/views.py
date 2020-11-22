#Standard libraries
import json
import requests
import os
import random
#Django
from django.shortcuts import render, redirect
from django.conf import settings
#models
from apps.home.models import Username

# Create your views here.
def home(request, page):
    page = int(page)
    if request.method == 'POST':
        username = request.POST['username']
        #Get username info from GH and save it on DB
        _data_from_github(username)
        return redirect('/')

    data=[]
    all_users = Username.objects.all()
    for user in all_users:
        user_info = json.loads(user.username_info)
        repos_info = json.loads(user.repos_info)
        user_info['repos']=repos_info
        data.append(user_info)
        random.shuffle(data)

    context = {
        'users' : data,
    }
    return render(request, 'index.html', context)

def _data_from_github(username):
    s = requests.Session()
    user = s.get('https://api.github.com/users/' + username)
    user_dict = json.loads(user.text)
    if 'message' in user_dict.keys():
        pass
    else:
        repos = s.get('https://api.github.com/users/' + username + '/repos')
        #Create new user in DB
        new_user = Username.objects.create()
        new_user.username = username
        new_user.username_info = user.text
        new_user.repos_info = repos.text
        new_user.save()
