#Grove pi uzerinde python3 kullanarak DHT 11 sensor ile sicaklik ve nem degerlerini alip influx db ye yazdirma.
import grovepi
import time
import requests
dht_sensor_port=4
dht_sensor_type=0
data=open('data.txt','w')
while True:
                [ temp,hum ] = grovepi.dht(dht_sensor_port,dht_sensor_type)
                print ('Temp: '+ str(temp) + '*C' + '\tHumidity:' + ' %'+ str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
                time.sleep(1)
                data.write('temperature,' + 'temp='+ str(temp) + ' ' + 'hum=' +str(hum) + ' ' + str(time.strftime("%s",time.gmtime())))
                response = requests.post('http://yourip:8086/write?db=mydb', data=f'temperature temp={temp} \n temperature hum={hum}')
                data.write('\n')
