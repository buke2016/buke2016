class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_right(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = find_left(nums, target), find_right(nums, target)
        if left <= right:
            return [left, right]
        else:
            return [-1, -1]
        
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = search_range(nums1, target1)
print(result1)  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
result2 = search_range(nums2, target2)
print(result2)  # Output: [-1, -1]

nums3 = []
target3 = 0
result3 = search_range(nums3, target3)
print(result3)  # Output: [-1, -1]

