class Solution:
    def searchRange(self, nums, target):
        def find_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def find_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        left, right = find_left(nums, target), find_right(nums, target)
        if left < right:
            return [left, right - 1]
        else:
            return [-1, -1]

nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = Solution().searchRange(nums1, target1)
print(result1)  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
result2 = Solution().searchRange(nums2, target2)
print(result2)  # Output: [-1, -1]

nums3 = []
target3 = 0
result3 = Solution().searchRange(nums3, target3)
print(result3)  # Output: [-1, -1]
