import math

for n in range (1, 100):

  count=0
  for x in range (-n, n):
    for y in range (-n, n):
      if ((2*x*x < n*n) and (2*y*y < n*n)):
        count=count+1
  print(count)
