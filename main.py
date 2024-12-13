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

import requests
from datetime import datetime
import time


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
        


def main():

    CMUObject = CMULibraryServices()
    cmu_account = str(input("CMU ACCOUNT : "))

    # Login
    account_status = CMUObject.checkaccount(cmuaccount=cmu_account)

    print("Logged In CMU ACCOUNT : ", cmu_account)
    print(account_status)

    system = CMUObject.checksystem()

    fake_time = "22:09:40"
    real_time = system['dataconfigs'][0]['TimeAutoOpen']
    end_timestamp = datetime.now().timestamp() + 5

    for i in range(1000):
        current_time = datetime.now().strftime("%H:%M:%S")
        timestamp = datetime.now().timestamp()
        print(current_time)
        print(timestamp)
        if(timestamp > end_timestamp+5):
            print("ถึงเวลากดแล้ว")
            print(system['dataconfigs'])
            if(system['dataconfigs'][0]['Btnnetflix'] == '0'):
                print("--------------------------------")
                print("รับ Netflix สำเร็จ!")
                print("Time Receieve : ", current_time)
                print("--------------------------------")
                break
        else:
            print("Waiting....")
        time.sleep(1)

main()