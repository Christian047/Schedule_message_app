import time
import requests
import schedule

def send_message():
    resp = requests.post('https://textbelt.com/text',
                         {'phone': '+2349027989868',  # Include the country code (+234) and remove the leading zero
                          'message': 'Hey Goodmorning',
                          'key': 'textbelt'}  # Replace 'textbelt' with your actual API key
                         )

    print(resp.json())
    print('Done')

send_message()


schedule.every(10).seconds.do(send_message)
    
while True:
    schedule.run_pending()
    time.sleep(1)

