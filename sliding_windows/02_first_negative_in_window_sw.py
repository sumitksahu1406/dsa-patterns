# I have solved it using the sliding window method.
#
# Given an array arr[] and a positive integer k, find the first negative integer for each and every window (contiguous subarray) of size k.
#
# Note: If a window does not contain a negative integer, then return 0 for that window.
#
# Approach:
# - Use a sliding window of size k and a queue to keep track of negative numbers in the current window.
# - As the window moves, add new negative numbers to the queue and remove numbers that are out of the window.
# - For each window, the first element in the queue (if any) is the first negative integer; otherwise, output 0.
#
# Examples:
#
# Input: arr[] = [-8, 2, 3, -6, 10], k = 2
# Output: [-8, 0, -6, -6]
#
# Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
# Output: [-1, -1, -7, -15, -15, 0]
#
# Input: arr[] = [12, 1, 3, 5], k = 3
# Output: [0, 0]
from collections import deque

def first_negative_in_window(arr, k):
    n=len(arr)
    result = []
    q = deque()   # store indices of negative numbers

    for i in range(n):
        # Step 1: add new element if negative
        if arr[i] < 0:
            q.append(i)
        
        # Step 2: when window of size k is formed
        if i >= k-1:
            # Remove elements which are out of window
            while q and q[0] <= i - k:
                q.popleft()

            # Step 3: get the answer
            if q:
                result.append(arr[q[0]]) # first negative in window
            else:
                result.append(0)

    return result

print(first_negative_in_window(arr = [12, -1, -7, 8, -15, 30, 16, 28], k=3))