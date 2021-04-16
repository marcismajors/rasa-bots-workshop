# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import requests
from typing import Any, Text, Dict, List, Tuple
from requests.exceptions import HTTPError
from requests.exceptions import Timeout

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

URL = "https://api.chucknorris.io/jokes/random"

def getResponse(url: Text, timeout = 3) -> Tuple[bool, Dict]:
    try:
        response = requests.get(url, timeout = timeout)
    except Timeout:
        return False, { "error": f'The request timed out in {timeout}s' } # Failed because of timeout
    except Exception as err:
        return False, { "error": f'An error has occurred: {err}' } # Failed because of some other error
    else:
        if response.status_code == 200:
            return True, response.json() # Success, return parsed json as Dict
        else:
            return False, { "error": f'Status code: {response.status_code}' } # Failed as didn't get 200, so something went wrong

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_get_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        success, response = getResponse(URL)
        if success:
            joke = response['value']
            print(joke)
        else:
            joke = "You can see Chuck Norris's charisma from space."
            print(f'Failed to get a joke from {URL}. {response["error"]}')

        dispatcher.utter_message(text=joke)

        return []
