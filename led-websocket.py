import asyncio
import websockets
import json
from urllib.request import urlopen

import RPi.GPIO as GPIO

with urlopen('https://raw.githubusercontent.com/Rajeshzealster/led-websocket/main/conf.json') as url:
    data = json.loads(url.read().decode())
    PIN = int(data['pin'])
    

with open('/tmp/system-service/env.json','r') as conf:
    data = json.loads(conf.read())
    url = data['websocket_url']


URL = 'ws://'+url
STATE = False


async def client():
    try:
        async with websockets.connect(URL) as server:
            info = {}
            info['type'] = 'actuator'
            await server.send(json.dumps(info))

            while True:
                message = await server.recv()
                message = json.loads(message)
                print('Actuation : '+str(message['value']))

                global STATE, PIN

                if STATE:
                    GPIO.output(PIN, GPIO.LOW)
                    STATE = not STATE
                else:
                    GPIO.output(PIN, GPIO.HIGH)
                    STATE = not STATE

    except Exception as e:
        print(str(e))


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
asyncio.run(client())
