# https://medium.com/@AvocadoandToast/a-beginners-guide-to-big-o-notation-793d654973d
# Find target 22 (i.e. return its index)in a sorted list
# Here we use Binary Search algorithm because its time complexity is O(log n)
def binarySearch(sortedlist, target):
 left = 0
 right = len(sortedlist) - 1
 while (left <= right):
  mid = (left + right)/2
  if (sortedlist(mid) == target):
   return mid
  elif(sortedlist(mid) < target):
   left = mid + 1
  else:
   right = mid - 1
# If target is not in the list, return -1
 return -1
binarySearch([1,3,9,22],22)
# return 3