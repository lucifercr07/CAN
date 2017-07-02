#lambda expression use for checking if rpm and vibration metrics exceeds a specified limit

rpm = [45,20,30,50,52,35,55,65,55,48]
rpm_limit = 45
vibration = [0.455,0.56,0.5222,0.523,0.66,0.43,0.555,0.234,0.533,0.777]
vibration_limit = 0.500

def check():
    result = list(map(lambda x,y: 1 if (x>=rpm_limit and y>=vibration_limit) else 0, rpm,vibration))
    if(result.count(1)>=5):
        return 1
    return 0

print(check())