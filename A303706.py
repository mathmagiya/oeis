import math

tan=math.sqrt(3)/3
for n in range (1, 70):
  count=0
  count1=0
  for x in range (-n, n):
    for y in range (-n, n):
      if (x*x+y*y<n*n and y>-tan*x+tan*n):
        count=count+1
      if (x*x+y*y<n*n and y<-n/2):
        count1=count1+1
  print(2*count+count1)
