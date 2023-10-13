class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat_all(speed):
            hours_needed = sum((pile / speed) for pile in piles)
            return hours_needed <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Create an instance of the Solution class
sol = Solution()

# Call the minEatingSpeed method
result = sol.minEatingSpeed([3, 6, 7, 11], 8)
print(result)
