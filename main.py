import random
import requests
import time

plot_interval = 60
url = 'https://api.thingspeak.com/update?api_key=34QM7GAI4PRG8HXF'
payload = {'field1': '0'}

duration = 24 * 60 * 60
end_time = time.time() + duration

while time.time() < end_time:
    payload['field1'] = str(random.randint(1, 30))    
    r = requests.get(url, params=payload)

    if r.status_code != 200:
        print r.status_code
        
    time.sleep(plot_interval)

