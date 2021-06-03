############------------ IMPORTS ------------############
import requests


############------------ FUNCTIONS ------------############
def get_random_dad_joke():
    '''
     hitting "random joke" endpoint
     https://icanhazdadjoke.com/api#fetch-a-dad-joke
    '''
    joke = requests.get('https://icanhazdadjoke.com',
                        headers={'Accept': 'application/json'}).json()

    print(joke['joke'])


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_random_dad_joke()
    '''
    What’s E.T. short for? He’s only got little legs.
    '''
