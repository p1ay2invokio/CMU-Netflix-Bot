# https://services.library.cmu.ac.th/moviestreaming/api/configs/checksystem
# Request POST
# {
#     "Action": "checksystem"
# }

# https://services.library.cmu.ac.th/moviestreaming/api/account/checkaccount
# Request POST
# {
#     "Action": "checkaccount",
#     "cmuitaccount": "rattanon_boonmata@cmu.ac.th"
# }

# https://misapi.cmu.ac.th/cmuitaccount/v1/api/cmuitaccount/basicinfo
# Request GET
# Bearer 311HKAcVZX2mwG5acu52CTAgZHmHuwAD

# https://app.scmc.cmu.ac.th/api/v2/history_scan

# !Important TOKEN[LIBRARY TOKEN]
# https://services.library.cmu.ac.th/moviestreaming/cmumobileacceptprivacy?token="YOUR CMU TOKEN"	GET PUT TOKEN
# https://services.library.cmu.ac.th/moviestreaming/cmumobile?token=7d6tx2rWNScSwMKmQv0RYhvMXTD488cF //

# Find your token with mitm

# https://app.scmc.cmu.ac.th/api/app/29/goto?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ODg1NDYsImlhdCI6MTcyMjIzNTQ3OH0.DEYg-aExybY3RksG5lSdwAOwJ3SuM5MfD3BXAd-OEDM it will redirect to library services with token

uri_system = 'https://services.library.cmu.ac.th/moviestreaming/api/configs/checksystem'
uri_account = 'https://services.library.cmu.ac.th/moviestreaming/api/account/checkaccount'
uri_auth_phone = 'https://services.library.cmu.ac.th/moviestreaming/cmumobileacceptprivacy'
uri_get_netflix ='https://services.library.cmu.ac.th/moviestreaming/api/account/getnetflix'

MY_APP_CMU_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ODg1NDYsImlhdCI6MTcyMjIzNTQ3OH0.DEYg-aExybY3RksG5lSdwAOwJ3SuM5MfD3BXAd-OEDM'
MY_LIB_CMU_TOKEN = ''

import requests
from datetime import datetime
import time
from colorama import Fore, Back, Style, init
import os

init()

#before use this you have to mitm proxy for know your token to put it into this

class CMULibraryServices:
    def checksystem(self):

        payload = {
            "Action": "checksystem"
        }

        response = requests.post(uri_system, json=payload)

        return response.json()

    def checkaccount(self, cmuaccount):
        payload = {
            "Action": "checkaccount",
            "cmuitaccount": cmuaccount
        }

        response = requests.post(uri_account, json=payload)

        return response.json()

    def getNetflix(self, cmu_token):
        payload = {
            "Action": "getnetflix",
            "token": cmu_token
        }

        response = requests.post(uri_auth_phone, params=payload['token'])

        return response.json()
        

log = False

def main():

    CMUObject = CMULibraryServices()
    
    cmu_account = str(input("CMU Token : "))

    if(len(cmu_account) < 3):
        print("must fill the CMU Token correct follow the format!")
    else:
        # Login
        account_status = CMUObject.checkaccount(cmuaccount=cmu_account)

        print("Logged In CMU ACCOUNT : ", cmu_account)
        print(account_status)

        # fake_time = "22:09:40"
        # real_time = system['dataconfigs'][0]['TimeAutoOpen']

        # end_timestamp = datetime.now().timestamp() + 5 # 5 sec after this will got netflix

        collision_time = "02/05/2025 14:00:00"
        collision_time_object = datetime.strptime(collision_time, "%m/%d/%Y %H:%M:%S")
        timestamp_end = int(collision_time_object.timestamp())


        for i in range(1000):
            system = CMUObject.checksystem()
            current_time = datetime.now().strftime("%H:%M:%S")
            timestamp = datetime.now().timestamp()

            diff = timestamp_end - timestamp

            hours = diff // 3600
            minutes = (diff % 3600) // 60
            seconds = diff % 60
            days = hours / 24

            print(system)

            print(Fore.WHITE + "-----------------------------------------------")
            print(Fore.GREEN + "Available : " + str(system['dataaccounts']['total']))
            print(Fore.WHITE + "-----------------------------------------------")
            print(Fore.GREEN + "NOW : " + str(current_time))
            print(Fore.YELLOW + "Timestamp : " + str(timestamp))
            print(Fore.YELLOW + "End Timestamp : " + str(timestamp_end))
            print(Fore.YELLOW + "Count Down : "+ str(int(days)) + "days : "  + str(int(hours)) + "h : " + str(int(minutes)) + "m : " + str(int(seconds)) + 's')
            if(system['dataconfigs'][0]["Btnnetflix"] == '1'):
                print("กดปุ่มได้แล้ว")
                # ใช้จริงต้องไม่ใช่ Token นี้ แต่เป็น LIB_Token
                # อันนี้ทดลอง For Testing
                CMUObject.getNetflix(cmu_token=cmu_account)
                if(account_status['status']):
                    print("รับ Netflix สำเร็จ!")
                    print(account_status['data'][0]['EmailAddress'])
                    print(account_status['data'][0]['Password'])
                    break
            else:
                print(Fore.CYAN + "Waiting....")
            time.sleep(0.1)
            if(log == True):
                os.system("cls")

main()