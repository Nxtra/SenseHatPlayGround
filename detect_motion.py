from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)

print("starting")

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
        print("whaa")
        sleep(1)
    else:
        sense.clear()
    
    