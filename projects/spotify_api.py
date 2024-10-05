
import requests 
from django.shortcuts import redirect
from django.http import JsonResponse
from datetime import datetime
import urllib.parse

CLIENT_ID='b61b4c001f0a4aa5b1a0da3b19882d5a'
CLIENT_SECRET='7913cc051a7e4c8f8b2871c21ee8f8de'
REDIRECT_URI='http://localhost:8000/callback'

AUTH_URL='https://accounts.spotify.com/authorize'
TOKEN_URL='https://accounts.spotify.com/api/token'
API_BASE_URL='https://api.spotify.com/v1'

def index(request):
    return JsonResponse({'message': 'Welcome to ad-free Spotify App!'})

def login(request):
    scope='user-read-private user-read-email'
    params={
        'client_id':CLIENT_ID,
        'response_type':'code',
        'scope':scope,
        'redirect_uri':REDIRECT_URI,
        'show-dialog':True
    }

    auth_url=f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    return redirect(auth_url)

def callback(request):
    if 'error' in request.GET:
        return JsonResponse({"error": request.GET['error']})
    
    elif 'code' in request.GET:
        req_body={
            'code':request.GET['code'],
            'grant_type': 'authorization_code',
            'redirect_uri':REDIRECT_URI,
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET
        }

        response=requests.post(TOKEN_URL, data=req_body)
        token_info=response.json()

        request.session['access_token']=token_info['access_token']
        request.session['refresh_token']=token_info['refresh_token']
        request.session['expires_in']= datetime.now().timestamp() + token_info['expires_in']

        return redirect('/playlist')
    

def get_playlist(request):
    if 'access_token' not in request.session:
        return redirect('/login')
    
    if request.session['expires_in'] < datetime.now().timestamp():
        return redirect('/refresh-token')
    
    headers={
        'Authorization':f"Bearer {request.session['access_token']}"
        }
    
    response= requests.get(API_BASE_URL + 'me/playlists', headers=headers)
    playlist= response.json()
    print("Access Token: ", request.session['access_token'])
    return JsonResponse(playlist)

def refresh_token(request):
    if 'refresh-token' not in request.session:
        return redirect('/login')
    
    if request.session['expires_in'] < datetime.now().timestamp():
        req_body={
            'grant_type': 'refresh_token',
            'refresh_token':request.session['refresh_token'],
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET
        }

        response= requests.post(TOKEN_URL, data=req_body)
        new_token_info=response.json()
        request.session['access_token']=new_token_info['access_token']
        request.session['refresh_token']=new_token_info['refresh_token']
        request.session['expires_in']= datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/playlist')

