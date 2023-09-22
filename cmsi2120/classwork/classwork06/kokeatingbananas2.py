def minEatingSpeed(piles, h):
    def canFinish(piles, k, h):
        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + k - 1) // k
        return hours_needed <= h

    left = 1
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if canFinish(piles, mid, h):
            right = mid
        else:
            left = mid + 1

    return left

# Example usage:
piles1 = [3, 6, 7, 11]
h1 = 8
print(minEatingSpeed(piles1, h1))  # Output: 4

piles2 = [30, 11, 23, 4, 20]
h2 = 5
print(minEatingSpeed(piles2, h2))  # Output: 30

piles3 = [30, 11, 23, 4, 20]
h3 = 6
print(minEatingSpeed(piles3, h3))  # Output: 23
