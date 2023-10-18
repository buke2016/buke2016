def getMinMax(a,n):
  if n == 0:
    return None
  minimum = maximum = a[0]
  for i in range(1,n):
    if a[i] < minimum:
      minimum = a[i]
    elif a[i] > maximum:
      maximum = a[i]

  return minimum, maximum

N = 5
A = [1,345,234,21,56789]
min_value, max_value = getMinMax(A,N)

print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")