
"""         SPOTIFY PLAYLIST ACCESS         """

import requests 
from flask import Flask, redirect, request, jsonify, session
import urllib.parse
from datetime import datetime, timedelta


# import secrets
# print(session)
app=Flask(__name__)

app.secret_key='61f459a6a70c3e40b719212d1d6942a3'

CLIENT_ID='b61b4c001f0a4aa5b1a0da3b19882d5a'
CLIENT_SECRET='7913cc051a7e4c8f8b2871c21ee8f8de'
REDIRECT_URI='http://localhost:5000/callback'

AUTH_URL='https://accounts.spotify.com/authorize'
TOKEN_URL='https://accounts.spotify.com/api/token'
API_BASE_URL='https://api.spotify.com/v1'

@app.route('/')
def index():
    return "Welcome to ad-free Spotify App <a href='/login'>Login with Spotify</a>"

@app.route('/login')
def login():
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

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": {request.args['error']}})
    
    elif 'code' in request.args:
        req_body={
            'code':request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri':REDIRECT_URI,
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET
        }

        respose=requests.post(TOKEN_URL, data=req_body)
        token_info=respose.json()


        session['access_token']=token_info['access_token']
        session['refresh_token']=token_info['refresh_token']
        session['expires_in']= datetime.now().timestamp()+ token_info['expires_in']

        return redirect('/playlist')
    

@app.route('/playlist')
def get_playlist():
    if 'access_token' not in session:
        return redirect('/login')
    
    if session['expires_in']<datetime.now().timestamp():
        return redirect('/refresh-token')
    headers={
        'Authorization':f"Bearer {session['access_token']}"
    }
    # https://api.spotify.com/v1/me/player/recently-played
    response= requests.get(API_BASE_URL + '/me/playlists', headers=headers)
    # response= requests.get(API_BASE_URL + '/me/player/recently-played', headers=headers)
    playlist= response.json()
    # print("Access Token: ", session['access_token'])
    return jsonify(playlist)

@app.route('/refresh-token')
def refresh_token():
    if 'refresh-token' not in session:
        return redirect('/login')
    
    if session['expires_in']<datetime.now().timestamp():
        req_body={
            'grant_type': 'refresh_token',
            'refresh_token':session['refresh_token'],
            'client_id':CLIENT_ID,
            'client_secret':CLIENT_SECRET
        }

        response= requests.post(TOKEN_URL, data=req_body)
        new_token_info=response.json()
        session['access_token']=new_token_info['access_token']
        session['refresh_token']=new_token_info['refresh_token']
        session['expires_in']= datetime.now().timestamp()+ new_token_info['expires_in']

        return redirect('/playlist')


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)


