############------------ IMPORTS ------------############
import requests


############------------ FUNCTIONS ------------############
def get_random_dad_joke():
    joke = requests.get('https://icanhazdadjoke.com',
                        headers={'Accept': 'application/json'}).json()

    print(joke)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_random_dad_joke()
    '''
     {'id': 'FdN7hiG6Uvc', 
     'joke': "Why can't eggs have love? They will break up too soon.", 
     'status': 200}
    '''
