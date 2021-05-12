import random
import math
from twilio.rest import Client

def generateOtp(mobile):
    values= "0123456789abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = len(values)
    otp = ""
    for i in range(6):
        otp += values[math.floor(random.random()*l)]
    message = "Your otp is "+otp
    account_sid = 'ACf6ee7d1ba7bd910fcc69246d9f0de6fb'
    auth_token = 'aaa5eb8ea4e3d59767add19b3ca303b9'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=str(message),
                         from_='+18575870863',
                         to='+91'+str(mobile)
                     )
    print(otp)
    print(message.sid)
    return otp
