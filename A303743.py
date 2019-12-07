for n in range (1, 42):
  count=0
    for x in range (-n, n):
      for y in range (-n, n):
        for z in range (-n, n):
          if (x*x+y*y+z*z>n*n and x>-n and x<n and y>-n and y<n and z>-n and z<n):
            count=count+1
  print(count)
