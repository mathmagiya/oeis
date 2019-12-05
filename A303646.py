import math

for n in range (1, 100):
  count=0
    for x in range (-math.ceil(math.sqrt(2)*n), math.ceil(math.sqrt(2)*n)):
      for y in range (-math.ceil(math.sqrt(2)*n), math.ceil(math.sqrt(2)*n)):
        if (x*x+y*y>n*n and abs(x)+abs(y)<n*math.sqrt(2)):
          count=count+1
  print(count)
