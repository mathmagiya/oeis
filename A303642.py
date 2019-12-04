import math

for n in range(1, 100):
  count = 0
  for x in range(0, n):
    for y in range(-n, n):
      if (x * x + y * y < n * n and x > n / math.sqrt(2)):
        count = count + 1
  print(4 * count)
