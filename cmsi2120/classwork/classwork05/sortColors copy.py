class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,mid,right = 0,0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[left],nums[mid] = nums[mid], nums[left]
                left += 1
                mid +=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[right]= nums[right], nums[mid] 
                right -= 1

solution = Solution()
nums1 = [2,0,2,1,1,0]
nums2 = [2,0,1]

solution.sortColors(nums1)
print(nums1)

solution.sortColors(nums2)
print(nums2)