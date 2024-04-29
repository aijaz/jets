import requests

def sendlog(msg):
    # debug(msg)
    server = 'https://secure.mypi.org/train/log'
    data = {"log": msg}
    requests.post(server, json=data)

def debug(msg):
    # pass
    print(msg)
