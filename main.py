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

uri_system = 'https://services.library.cmu.ac.th/moviestreaming/api/configs/checksystem'
uri_account = 'https://services.library.cmu.ac.th/moviestreaming/api/account/checkaccount'
uri_get_netflix ='https://services.library.cmu.ac.th/moviestreaming/api/account/getnetflix'

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

        response = requests.post(uri_get_netflix, json=payload)

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

        collision_time = "01/01/2025 14:00:00"
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

            print(Fore.WHITE + "-----------------------------------------------")
            print(Fore.GREEN + "Available : " + str(system['dataaccounts']['total']))
            print(Fore.WHITE + "-----------------------------------------------")
            print(Fore.GREEN + "NOW : " + str(current_time))
            print(Fore.YELLOW + "Timestamp : " + str(timestamp))
            print(Fore.YELLOW + "End Timestamp : " + str(timestamp_end))
            print(Fore.YELLOW + "Count Down : "+ str(int(days)) + "days : "  + str(int(hours)) + "h : " + str(int(minutes)) + "m : " + str(int(seconds)) + 's')
            if(timestamp > timestamp_end):
                print("ถึงเวลากดแล้ว")
                print(system['dataconfigs'])
                if(system['dataconfigs'][0]['Btnnetflix'] == '1'):
                    response = CMUObject.getNetflix(cmu_account)
                    if(response.statusCode == 200):
                        print("รับ Netflix สำเร็จ!")
                    break
            else:
                print(Fore.CYAN + "Waiting....")
            time.sleep(0.5)
            if(log == True):
                os.system("cls")

main()