#lambda expression use for checking if rpm metric exceeds a specified limit

rpm = [45,20,30,50,52,35,55,65]
rpm_limit=45
    
def check():
    result = list(filter(lambda x: x>=rpm_limit, rpm))
    if(len(result)>=5):
        return 1
    return 0

print(check())