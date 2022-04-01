from machine import ADC, Pin
import time
adc = ADC(Pin(26))
v1=0
t1=0
while 1:
 adc2= adc.read_u16()
 v1= adc2 * 3,3 
 v1= v1/ 65535
 t1= v1 / 0.01
 print("La temperatura es: {:.2f}°C".format(t1))
 time.sleep(1)
