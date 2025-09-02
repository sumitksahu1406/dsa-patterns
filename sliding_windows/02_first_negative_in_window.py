# I have solved it using brute force approach.
# Link: https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
# Given an array arr[] and a positive integer k, find the first negative integer for each and every window (contiguous subarray) of size k.
#
# Note: If a window does not contain a negative integer, then return 0 for that window.
#
# Examples:
#
# Input: arr[] = [-8, 2, 3, -6, 10], k = 2
# Output: [-8, 0, -6, -6]
# Explanation:
# Window [-8, 2] First negative integer is -8.
# Window [2, 3] No negative integers, output is 0.
# Window [3, -6] First negative integer is -6.
# Window [-6, 10] First negative integer is -6.
#
# Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
# Output: [-1, -1, -7, -15, -15, 0]
# Explanation:
# Window [12, -1, -7] First negative integer is -1.
# Window [-1, -7, 8] First negative integer is -1.
# Window [-7, 8, -15] First negative integer is -7.
# Window [8, -15, 30] First negative integer is -15.
# Window [-15, 30, 16] First negative integer is -15.
# Window [30, 16, 28] No negative integers, output is 0.
#
# Input: arr[] = [12, 1, 3, 5], k = 3
# Output: [0, 0]
# Explanation:
# Window [12, 1, 3] No negative integers, output is 0.
# Window [1, 3, 5] No negative integers, output is 0.

def first_negative_in_window(arr, k):
    n = len(arr)
    result = []

    # Loop over all possible windows
    for i in range(n - k + 1):
        found = False

        # Scan the window of size k
        for j in range(i, i + k):
            if arr[j] < 0:
                result.append(arr[j])  # first negative
                found = True
                break

        # If no negative found in this window
        if not found:
            result.append(0)

    return result


# Example runs
print(first_negative_in_window([-8, 2, 3, -6, 10], 2))  # [-8, 0, -6, -6]
print(first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3))  # [-1, -1, -7, -15, -15, 0]
print(first_negative_in_window([12, 1, 3, 5], 3))  # [0, 0]