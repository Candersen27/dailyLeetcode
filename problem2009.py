"""
Problem 2009: Minimum Number of Operations to Make Array Continuous (hard)

You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

All elements in nums are unique

The difference between the maximum element and the minimum element in nums equals nums.length - 1

For Example, 
    nums = [4, 2, 5, 3] is continuous
    nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous

Constraints:
    1 <= nums <= 10^5
    1 <= nums[i] <= 10^9


Example 1:
    Input: nums = [4, 2, 5, 3]
    Output: 0
    Explanation: nums is already continuous

Example 2:
    Input: nums = [1, 2, 3, 5, 6]
    Output: 1
    Explanation: One possible solution is to change the last element to 4.
        The resulting array is [1,2,3,5,4], which is continuous.



Strategy:

    One way to tackle this problem is to use the sliding window algorithm.
    
    To start off, we want to sort the array

    Then we will remove any duplicates in the array.

    Next we will take a slice of the array starting at the beginning. set left = 0, right = 0 and slice the array and label it window from left:right

    Goal: we are trying to find the largest valid window we can.  If the range of a window (max - min) is smaller than the length of nums, a window is valid.

    If the range of the values in window are smaller than the length of nums, then our window is valid, record the size of the window and compare it to the largest window we've found so far.  Replace the largest window value if necessary, then add one to right, and slice a new window.

    If the range of the values in the window are larger than the length of nums, then the window is invalid.  Add one to left, and slice a new window.

    Keep going through the entire array.  At the end we will have a value associated with the largest valid window we could make with the array.

    This number shows us how many numbers we do not have to change.  We want to know how many we do have to change, so take the length of the original array nums (including duplicates) and subtract the size of our largest window.  The result will be our return value. 



"""
from collections import deque

class Solution:
        # We need to use deque instead of pop later on for time complexity reasons on very large nums length
    
    def minOperations(self, nums):
        
        # Start off by handling the edge case where the array has only one element
        if len(nums) == 1:
            return 0

        # Record the original size of nums with duplicates included
        numsLengthInitial = len(nums)

        # Remove duplicates by changing nums into a set, then back to a list. Sets can not contain duplicates.
        nums_set = set(nums)
        nums = list(nums_set)

        # sort nums
        nums = sorted(nums)

        # Initialize windowEnd. We will use this to determine the range of our window.
        windowEnd = 1

        # Initialize largestWindow.  This variable will eventually show us the number of elements we do not need to change.
        largestWindow = 0

        # Initialize our window, Python slices are up to but not including, so nums[0:1] will only give us the first element.
        # We set window to be a deque instead of a list so that we can pop items from the left side in O(1) time complexity.
        window = deque(nums[0:windowEnd])

        # Keep checking windows until the range of the windowEnd variable goes past the length of nums
        # note its important that we avoid any actions with time complexity n in our while loop.  When very large nums sets are involved, an n^2 time complexity will kill the algorithm.
        while windowEnd <= len(nums):
        
            # We can assign the last and first values of the window as max and min respectively because the list, and therefore any given window in the list is sorted.
            maxVal = window[-1]
            minVal = window[0]

            # If max - min >= len(nums) then there are values that must be changed in this window.
            if maxVal - minVal >= numsLengthInitial:
                # Remove the first element from the window
                window.popleft()
                
            # This is a valid window
            else:
                # First check to see if it is the largest window we have seen so far. If so, update largestWindow
                if len(window) > largestWindow:
                    largestWindow = len(window)

                # increment windowEnd, signifying a window expanding to the right.  If windowEnd grows larger than len(nums) here we are finished and will be spit out of the loop
                if windowEnd < len(nums):
                    window.append(nums[windowEnd])

                windowEnd += 1
                

        
        # After coming out of the while loop, we will have a largestWindow value equal to the total number of elements which wont have to be changed.  To find the total number of elements that do, just subtract from numsLengthinitial.

        return numsLengthInitial - largestWindow 



Sol = Solution

Q1 = [4,2,6,3]
Q2 = [1,2,3,5,12]
Q3 = [3,8,2,1,9,5]
Q4 = [1,10,100,1000]
Q5 = [8,5,9,9,8,4]
Q6 = [41,33,29,33,35,26,47,24,18,28]

print(f"answer: {Sol.minOperations(Sol, Q1)}")
print(f"answer: {Sol.minOperations(Sol, Q2)}")
print(f"answer: {Sol.minOperations(Sol, Q3)}")
print(f"answer: {Sol.minOperations(Sol, Q4)}")
print(f"answer: {Sol.minOperations(Sol, Q6)}")