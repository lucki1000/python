import os

while True:
    os.system('cat /sys/class/thermal/thermal_zone0/temp ' + '> ' + '/home/pi/temperatur.out')
    f = open("/home/pi/temperatur.out", "r")
    ergebnis = int(f.readline())
    f.close()
    celcius = ergebnis / 1000
    print("Grad in Celcius: ", celcius, end='\r')
    os.system('sleep 5')
