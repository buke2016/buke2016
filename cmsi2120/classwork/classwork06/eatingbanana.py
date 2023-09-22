def can_finish_piles(piles, H, K):
    hours_needed = 0
    for pile in piles:
        hours_needed += -(-pile // K)  # Calculate hours needed to finish each pile
    return hours_needed <= H

def min_eating_speed(piles, H):
    left = 1  # Minimum possible eating speed
    right = max(piles)  # Maximum possible eating speed

    while left < right:
        mid = (left + right) // 2  # Calculate the midpoint as the eating speed
        if can_finish_piles(piles, H, mid):
            right = mid  # Search in the left half
        else:
            left = mid + 1  # Search in the right half

    return left  # Left is the minimum eating speed that allows Koko to finish all piles within H hours

# Example usage:
piles = [3, 6, 7, 11]
H = 8
result = min_eating_speed(piles, H)
print(result)  # Output: 4
