import requests
import json


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'jOP7Zf6c5xVBGyXLpz83RMKuleJFhUCwnvItQm29YDEbHkrS4inmrYWgRyFwHPOpvoBduNfesGCXQ2k0',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


send_sms("9306979702", "hy... it's me SWATI :)")
