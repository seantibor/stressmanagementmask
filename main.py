from adafruit_circutplayground.express import cpx
import time

while True:
    # get the temperature in F
    temp = cpx.temperature * 9 / 5 + 32
    print((temp,))  #Farenheight output for Mu plotting
    time.sleep(0.5)
    if temp > 91: # This is my initial theory for the stress levels and temperature
        cpx.pixels.fill((255,0,0))
    elif temp < 90:
        cpx.pixels.fill((0,255,0))
