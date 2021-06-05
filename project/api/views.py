############------------ IMPORTS ------------############
from django import shortcuts
import requests
from django.shortcuts import render
from django.http import HttpResponse


############------------ VIEWS ------------############
def main(request):
    '''
     hitting "random joke" endpoint
     https://icanhazdadjoke.com/api#fetch-a-dad-joke
    '''
    # joke = requests.get('https://icanhazdadjoke.com',
    #                     headers={'Accept': 'application/json'}).json()['joke']

    joke = "How do you fix a broken pizza? With tomato paste."

    context = {"joke": joke}

    return render(request, "jokes.html", context)
