for n in range (1, 100):
  count=0
  for x in range (0, n):
    for y in range (0, n):
      if (x*x+y*y<n*n and x+y>n):
        count=count+1
  print(4*count)
