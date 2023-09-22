import math
def min_eating_speed(piles, h):
        def can_eat_all(speed):
            hours_needed = sum(math.ceil(pile / speed) for pile in piles)
            return hours_needed <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1

        return left

    # Test cases
print(min_eating_speed([3, 6, 7, 11], 8))  # Output: 4
print(min_eating_speed([30, 11, 23, 4, 20], 5))  # Output: 30
print(min_eating_speed([30, 11, 23, 4, 20], 6))  # Output: 23
        