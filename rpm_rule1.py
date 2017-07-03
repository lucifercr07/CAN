rpm = [45,20,30,50,52,35,55,65]
rpm_limit=45
    
def check():
    x=0,i=0
    while(i<len(rpm)):
	    if(filter(lambda x: x>=rpm_limit, rpm)):
	    	x=x+1
	    	if(x>=5):
	    		return 1
	    else:
	    	x=0
		i=i+1
	return 0	


print(check())