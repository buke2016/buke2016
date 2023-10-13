# implement the binary search approach to solving Koko's problem
# by replacing each ... with a single expression or line of code

def minEatingSpeed2(piles: list[int], h: int) -> int:
        # Initalize the left and right boundaries(min and max possible speeds)
        left = 1
        right = max (piles)

        while left <= right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2
            hour_spent = 0

            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += (pile + middle - 1) // middle #math.ceil(pile/middle) used by professor since they specify ceil(pile/middle)

            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1

        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return left # professor used right as a return since under while loop, we specified 'left <= right'