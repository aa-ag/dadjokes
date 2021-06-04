############------------ IMPORTS ------------############
import requests
import time
import schedule
from django.shortcuts import render
from django.http import HttpResponse


############------------ VIEWS ------------############
def main(request):
    '''
     hitting "random joke" endpoint
     https://icanhazdadjoke.com/api#fetch-a-dad-joke
    '''
    joke = requests.get('https://icanhazdadjoke.com',
                        headers={'Accept': 'application/json'}).json()['joke']ß

    return HttpResponse(joke)
