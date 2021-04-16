import discord
import os
import requests

from typing import Text, Dict, Tuple
from requests.exceptions import HTTPError
from requests.exceptions import Timeout

rasa_url = 'http://localhost:5005/webhooks/rest/webhook'

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    payload={
        "sender":message.author.id,
        "message":message.content
    }
    
    success, rasa_response = postResponse(rasa_url, payload)
    
    if success:
        for response in rasa_response:
            if "text" in response:
                await message.channel.send(response["text"])
            if "image" in response:
                await message.channel.send(response["image"])
    else:
        print(f'Failed to get RASA bot response from {rasa_url}. {rasa_response["error"]}')
        await message.channel.send('I have some internal problems right now, cant answer')
    
def postResponse(url: Text, data: Dict, timeout = 3) -> Tuple[bool, Dict]:
    try:
        response = requests.post(url, json = data, timeout = timeout)
    except Timeout:
        return False, { "error": f'The request timed out in {timeout}s' } # Failed because of timeout
    except Exception as err:
        return False, { "error": f'And error has occured: {err}' } # failed because of some other error
    else:
        if response.status_code == 200:
            return True, response.json() # Success!!!
        else:
            return False, { "error": f'Status code {response.status_code}' } # Failed as didnt get 200      
    
client.run(os.getenv('TOKEN'))