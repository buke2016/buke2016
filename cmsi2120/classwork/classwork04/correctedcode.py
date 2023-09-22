class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat_all(speed):
            hours_needed = sum((pile - 1) // speed + 1 for pile in piles)
            return hours_needed <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Example usage:
sol = Solution()

piles1 = [3, 6, 7, 11]
h1 = 8
result1 = sol.minEatingSpeed(piles1, h1)
print(result1) 

piles2 = [30, 11, 23, 4, 20]
h2 = 5
result2 = sol.minEatingSpeed(piles2, h2)
print(result2)  

piles3 = [30, 11, 23, 4, 20]
h3 = 6
result3 = sol.minEatingSpeed(piles3, h3)
print(result3) 