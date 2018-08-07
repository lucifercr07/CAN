import os
for filename in os.listdir("."):
	if filename.startswith("Lucifer"):
	   os.rename(filename, filename+".mp4")
