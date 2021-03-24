import requests, time

time.sleep(3)

a = requests.request(
    'GET', 'https://api.stackexchange.com/2.2/questions?fromdate=1616371200&todate=1616544000&'
           'order=desc&sort=activity&tagged=python&site=stackoverflow')
b = a.json()
print(b)
