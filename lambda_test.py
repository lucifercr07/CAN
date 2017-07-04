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

rpm = [45,20,30,50,52,35,55,65,60,66,60]

rpm_limit=45

def check():
    max_consec = reduce(lambda acc, r: acc + 1 if r > rpm_limit else 0, rpm, 0)
    return 1 if max_consec >= 5 else 0
    
print(check())