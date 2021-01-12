import os,time
#Functions that gives the random number
def randomNum(max):
  num = os.getpid()*time.time_ns()%max
  return int(num)

print(randomNum(989))