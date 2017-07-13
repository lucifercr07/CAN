#lambda expression use for checking if rpm and vibration metrics exceeds a specified limit

rpm = [45,20,30,50,52,35,55,65,55,48,88]
rpm_limit = 45
vibration = [0.455,0.56,0.5222,0.523,0.66,0.43,0.555,0.634,0.533,0.777,0.566]
vibration_limit = 0.500

f = lambda x,y : 1 if (x>=rpm_limit and y>=vibration_limit) else 0

def check():
	print("Args: ",f.__code__.co_argcount)
	result,counter = 0,0
	for i in range(len(rpm)):
		result = f(rpm[i],vibration[i])
		counter = 0 if(result==0) else counter+1
		if(counter>=5):
			return 1
	return 0

print(check())