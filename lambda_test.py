import random
import time

def get_rpm():
    return random.randint(40,46)

def get_vibration():
    return random.uniform(0.300,0.600)

while(1):
    print("RPM: ",get_rpm())
    print("Vibration: ",get_vibration())
    time.sleep(1)
