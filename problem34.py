"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing orfer, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with 0(log n) runtime complexity

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3, 4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1, -1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1, -1]




"""



class Solution:
    def searchRange(self, nums, target):
        
        # Initialize the beginning and end of our search radius.  At first we check the entire list nums
        left = 0
        right = len(nums)

        #set up a flag that will let us know whether we found any values equal to the target.
        flag = False

        while left <= right:
            # Identify the median of the list
            mid = round((left + right)/2)

            if nums[mid] == target:
                # We found the target number, set the flag to true, and break out of the loop with information we need stored in mid.
                flag = True
                break
            
            # The target will be in the right half/larger values in the list.  Reassign left with the value to the right of the median, and re-enter the while loop.
            elif nums[mid] < target:
                left = mid + 1

            # The target will be in the legt half/smaller values in the list.  Reassign right with the value to the left of the median, and re-enter the while loop.
            else:
                right = mid - 1

        # If there were no target values in the list, we return [-1, -1]
        if not flag:
            return [-1, -1]


        # Now we have the index of where a target number is. From here we check to the left and the right to see how long the indices keep that target value. When we get a deviation, we know what our final return will be.

        # First check the right half of nums.

        # hold the value of mid in mid1 and mid2.  We want to change these values in different ways in the next two while loops and they both need the initial mid to begin.

        mid1 = mid
        mid2 = mid


        while mid1 >= left:
            # Check the current value of nums and index mid1 against the target, 
            if nums[mid1] < target:
                # Given a match, we know our left bound of our answer will be the index previous.  set finalLeft to that value and break out of the while loop.
                finalLeft = mid1 + 1
                break
            
            else:
                # This variable assignment is used so that if we make it all the way to left holding the target value, the last mid (which will be equal to left) will be registered as finalLeft.
                finalLeft = mid1
                # Set mid1 to access the previous index and move into the next iteration.
                mid1 = mid1 - 1


        
        # This loop operates the same as above except we are going in the opposite direction.
        while mid2 <= right:
            if nums[mid2] > target:
                finalRight = mid2 - 1
                break

            else:

                finalRight = mid2
                mid2 = mid2 + 1


        
        return [finalLeft, finalRight]
    



Sol = Solution

Q1, t1 = [5, 7, 7, 8, 8, 8, 10, 14, 17, 19], 8

Q2, t2 = [5,7,7,8,8,10], 6

Q3, t3 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 9], 2



print(Sol.searchRange(Sol, Q1, t1))
print(Sol.searchRange(Sol, Q2, t2))
print(Sol.searchRange(Sol, Q3, t3))
