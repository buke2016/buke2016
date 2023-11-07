#with decorator
import time
def time_func(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    res = func(*args, **kwargs)
    end = time.time()
    print(f"Elapsed time: {(end - start) * 1000:.3f}ms")
    return res
  return wrapper