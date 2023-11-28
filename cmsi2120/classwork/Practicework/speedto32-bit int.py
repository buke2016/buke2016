import numpy as np
speed_float = 40000.54
speed_int = np.int32(speed_float) # convert the speed to a 32-bit int
print(speed_int)
speed_int = np.int16(speed_float)
print(speed_int)

if abs(speed_float) > np.iinfo(np.int16).max:
  print("***Error, cannot assign speed to 16-bit int. Will cause overflow.")
  # call command here to exit program
else:
  speed_int = np.int16(speed_float)

print(bin(2))
print((6))
print((110))
print(bin(6))
print(bin(110))
print(hex(1101110))
print(int(1101110))