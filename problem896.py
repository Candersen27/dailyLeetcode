"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.


Example 1:
    Input: nums = [1, 2, 2, 3]
    Output: true

Example 2:
    Input: nums = [6, 5, 4, 4]
    Output: true

Example 3:
    Input: nums = [1, 3, 2]
    Output: false  

"""



class Solution:
    def isMonotonic(self, nums):
        
        # Initialize this boolean it will determine whether we're checking to see if the list is monotonically increasing or monotonically decreasing later on
        isIncreasing = True

        # Any list of one element is always monotonic
        if len(nums) < 2:
            return True
        
        # First determine if the list should be decreaseing or should be increasing
        # Reduce the range by one because we dont want to make a check where i is the first of the two numbers to compare (there is no second number)
        for i in range(len(nums) - 1):
            # If numbers at the begining of the list are the same, we need to keep passing through them to get to an inequality.
            if nums[i] != nums[i + 1]:
                if nums[i] > nums[i + 1]:
                    # this means we can't be monotone increasing so the only way to pass true is if we're monotone decreasing
                    isIncreasing = False
                elif nums[i] < nums[i + 1]:
                    # this means we can't be monotone decreasing so the only way to pass true is if we're monotone increasing (dont need to make a change since its already intiailized as true, but for understanding)
                    isIncreasing = True

        
        if isIncreasing:
            
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # If we ever hit a number that is larger than the next one, we determine that the list is not monotone decreasing either.  Therefore we can return false.
                    return False
            
            # If we make it through the whole list without a False hit, we know the list is monotone increasing.
            return True

        if not isIncreasing:
            # Works the same as ifIncreasing is true as above except check for greater than instead of less than.
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
            
            return True
        


S = Solution
Q1 = [1]
Q2 = [6,5,5,4]
Q3 = [1,3,3,6]
Q4 = [3,1,7,5,8,9,4]

print(S.isMonotonic(S, Q1))
print(S.isMonotonic(S, Q2))
print(S.isMonotonic(S, Q3))
print(S.isMonotonic(S, Q4))