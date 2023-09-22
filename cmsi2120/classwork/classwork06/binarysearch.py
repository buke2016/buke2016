def binary_search(nums: list[int], target:int) -> int:
    left = 0
    right = len(nums)-1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
         return mid
      elif nums[mid] < target:
         left = mid + 1 
      else:
         right = mid - 1 
    return -1 
    for i in range(len(nums)):
       if nums[1] == target:
          return 1
    return - 1