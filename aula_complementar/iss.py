import time, requests 

parameters = {'lat': 40.78, 'lon': -73.96}
URL = "http://api.open-notify.org/iss-pass.json"
response = requests.get(url=URL, params=parameters)

data = response.json()
#print(type(data))
#print(data)

passagens = data['response']
volta = 0 

for i in passagens:
   cada = i['risetime']
   data_formatada = str(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(cada)))
   volta = volta + 1
   print("A passagem % sera na data % " % volta, data_formatada)
