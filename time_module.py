import time

#print(time.ctime(0))
#print(time.time())

#print(time.ctime(time.time())) #current date and time

time_object = time.localtime()
print(time_object)
time.strftime("%B %d %y %H:%M:%S",time_object)
print(time.localtime())