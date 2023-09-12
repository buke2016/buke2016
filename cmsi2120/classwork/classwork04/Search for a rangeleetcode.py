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
