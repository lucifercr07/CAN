#lambda expression use for checking if rpm metric exceeds a specified limit more than five times consecutively
#values which exceeds a certain limit are not saved in this case

rpm = [45,20,30,50,52,35,55,65,70,75,85]
rpm_limit=45

f = lambda x : 1 if x>=rpm_limit else 0

def check():
	result,counter = 0,0
	for i in range(len(rpm)):
		result = f(rpm[i])
		counter = 0 if(result==0) else counter+1
		if(counter>=5):
			return 1
	return 0

print(check())