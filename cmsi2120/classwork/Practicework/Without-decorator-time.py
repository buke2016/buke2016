# without decorator
import time
def add(num1: int, num2: int):
  start = time.time()
  sum_ = num1 + num2
  end = time.time()
  print(f"Elapsed time: {(end - start) * 1000:.3f}ms")

  return sum_

add(1, 2) # Elapsed time: 1.006ms