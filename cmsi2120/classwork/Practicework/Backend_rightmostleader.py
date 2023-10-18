class Solution:
    # Function to find the leaders in the array.
    def leaders(self, A, N):
        # Initialize the rightmost element as the leader since there are no elements to its right.
        leader = A[N - 1]
        
        # Create a list to store the leaders.
        leaders = [leader]
        
        # Traverse the array from right to left.
        for i in range(N - 2, -1, -1):
            # If the current element is greater than the leader, it becomes the new leader.
            if A[i] >= leader:
                leader = A[i]
                leaders.append(leader)
        
        # Reverse the list of leaders to maintain the original order.
        leaders.reverse()
        
        return leaders
