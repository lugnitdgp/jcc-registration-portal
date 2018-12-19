from urllib.parse import urlencode
from decouple import config
import hashlib
import requests

BASE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
auth_key = config('SECRET_KEY')
url = 'http://sms.globehost.com/api/sendhttp.php?'


def encode_base(num, array=BASE):
    if(num == 0):
        return array[0]
    retarr = []
    base = len(array)
    while num:
        num, res = divmod(num, base)
        retarr.append(array[res])
    retarr.reverse()
    return ''.join(retarr)[:6]


def generate(alphanum):
    short = (hashlib.md5(alphanum.encode())).hexdigest()
    short = int(short, 16)
    short = encode_base(short)
    return short


def send_message(team_name, team_id, contact):

    message = 'Your unique team ID for Junior Code Cracker 2k18 is ' + \
        team_id + '.Kindly take note and submit this at the event.'

    data = {
        'authkey': auth_key,
        'mobiles': contact,
        'message': message,
        'sender': 'GNULUG',
        'route': '4',
    }

    data_encoded = urlencode(data)
    r = requests.get(url + data_encoded)
    print('Message Sent Successfully !!')
    return r.status_code
