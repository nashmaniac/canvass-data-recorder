# build the sensor data & frequency
import random
import threading
import time
from datetime import datetime
import json

import requests

def send_data(id: int, backoff: int, message_count: int):
    print('Sensor-%d will send %d data every %d milliseconds' %
          (id, message_count, backoff))
    status = ["on", "off", "active", "inactive"]
    count = 0
    base_url = 'http://localhost:8000'
    path = '%s/recorder/api/v1/sensor-data/' % base_url
    while(count < message_count):
        count += 1
        pressure = round(
            (random.random() * random.randint(1, 200))+random.randint(1, 200), 2)
        temp = round((random.random() * random.randint(1, 200)) +
                     random.randint(1, 200), 2)
        data = dict(
            deviceId='sensor-%d' % id,
            timestamp=datetime.now().isoformat(),
            pressure=pressure,
            temperature=temp,
            status=status[random.randint(0, len(status)-1)]
        )
        json_object = json.dumps(data, indent=4)
        print('Sensor-%d sending data %d - %s' %
              (id, count, str(json_object)))        
        r = requests.post(path, data=data)
        # print(r.json())
        time.sleep(backoff/1000)
    print('Sensor-%d is done sending data' % id)


def run_simulation(n: int, lowest_backoff_time: int, highest_backoff_time: int, lowest_data_count: int, highest_data_count: int):
    random_time = [(random.randint(lowest_backoff_time, highest_backoff_time), random.randint(
        lowest_data_count, highest_data_count)) for i in range(n)]

    for i, entry in enumerate(random_time):
        t = threading.Thread(name="sensor-%d" % (i+1),
                             target=send_data, args=(i+1, entry[0], entry[1],))
        t.start()


if __name__ == '__main__':
    n = 15  # number of sensors
    lowest_backoff_time = 500
    highest_backoff_time = 1000
    lowest_data_count = 1000
    highest_data_count = 5000
    run_simulation(n, lowest_backoff_time, highest_backoff_time,
                   lowest_data_count, highest_data_count)
