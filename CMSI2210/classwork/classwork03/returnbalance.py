def odd(x):
  return x % 2 != 0
def balance(p,n,r,t):
  return p * (1+ r/n) ** (n*t)

print(odd(-35))
print(odd(3278947239863000))
print(balance(1000, 12, 0.03,5))