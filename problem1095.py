"""
1095. Find in Mountain Array

(This problem is an interactive problem)

You may recall that an arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

        given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
        If such an index does not exist, return -1.

        You can not access the mountain array directly. You may only access the array using a MountainArray interface:
            MountainArray.get(k) returns the element of the array at index k (0 - indexed).
            MountainArray.length() returns the length of the array

        Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
        Also, any solutions that attempt to circumvent the judge will result in disqualification.

        Constraints:
        
        3 <= mountain_arr.length() <= 1000
        0 <= target <= 10^9
        0 <= mountain_arr.get(index) <= 10^9


Strategy:
    This problem is a great opportunity to use a binary search algorithm.

    I will implement three total binary searches.  My first search will be to find the peak of the mountain, or max value in the array.
    The second search will traverse down the array to the left of the peak.
    The third and final search will traverse down the array to the right of the peak.

    Each search will happen inside a while loop.
    
    A binary search will look for the median index in the array, and compare it to something.  In the case of our first search, we will grab the value at the median index in the mountain array, and also grab the value at the index to the right of the median.
        
        If the value of the median index is less than the value of the next index, we can tell that we are ascending.  This means we are on the left side of the peak, so we want to move to the right.
        
        If the value of the median index is greater than the value of the next index, we can tell that we are descending.  This means we are on the right side of the peak, so we want to move to the left.

        To move left we reassign the value assocated with right to the current value of median. (initially left will be zero, the first index in the array. right will be len(array) - 1, the last index in the array.)

        To move right, we reassign the value associated with left to the current value of median.

        After this we recalculate a new median with the updated left and right values, and re-enter our loop

    Eventually we will hit an index where left is equal to right.  When this happens we are spit out of the loop, and will have our mountain peak!

    Quickly check an edge case where the peak ends up being the target.  If so, return the index of the peak.

    Now that we have the peak it is time to traverse down the mountain to look for our target.  We go left side first, because the problem asks for the minimum index for the target.  If there is a target on both the left side and the right side, we just want the left side, so no point traversing the right.

    Set right to the peak index, and left to zero and recalculate the median, then initiate another while loop:

    This while loop will last as long as left is less than right.
        In the loop, we get the value in the array at the median index, and assign it to focus
        Check to see if focus is equal to the target.  If so, return the value in median (associated with the index)

        if not, 
        compare focus to target.  if focus is larger, then we need to move further left.
            reassign right to median, and recalculate median, then re-enter the loop.
        if target is larger, we need to move further right.
            reassign left to median + 1, and recalculate median, then re-enter the loop.

        Eventually we will either hit our target, or traverse the side of the mountain without finding a target.

        If we dont find our target, we move on to the third binary search.

    
    The third binary search will be very similar to the second, except it will be a mirror image.  We are traversing the opposite side, so when we do our comparisons, when focus > target, we set left = median + 1, and when focus < target, we set right to median.

        Return the index of a target if it is found, but if not, then we conclude that the target is not in our array, and we return -1
        



"""

# First we set up the mountainArray class as its described in the problem.  We need to access this class in order to collect information about the array
class MountainArray:

    def __init__(self, arr) -> None:
        self.arr = arr

    def get(self, index):
        return self.arr[index]
    
    def length(self):
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target, mountain_arr):
        
    
        right = mountain_arr.length() - 1
        left = 0

        median = (right + left) // 2

        # for now top will hold a dummy value.  Eventually it will hold the index of the peak(max value) of the mountain array
        top = -99 

        #Check for the edge case where the first element is our target
        
        if mountain_arr.get(left) == target:
            return left
        

        # Our algorithm will be constantly changing the values of left, right and median.  However, part way through the algorithm we will often need to reset the value of right to their initial states. We'll hold this value in the following variable.
        initial_right = right

        # This while loop will find the top of the mountain.  It will end when left and right will be equal. 
        while left != right:
            
            focus = mountain_arr.get(median)
            next = mountain_arr.get(median + 1)
            
            # We are descending the mountain. To find the top we must go backward, set the new right to be the current next index and recalculate the new median.  Left will stay the same.
            if focus > next:
               
                right = median
                median = (right + left) // 2

            # We are ascending the mountain.  To find the top we must go forward. Set the new left to be the current median and recalculate the new median. Right will stay the same.
            elif focus < next:

                # check the edge case where the top of the mountain is the target value, only do this for ascending because there could be a descending and an ascending target, but we'll only want the ascending target in that case
                if focus == target:
                    return median   
                
                left = median + 1
                median = (right + left) // 2


        # after this loop finishes, both left and right should be equal to eachother, pointing to the index of the top of the mountain.  Assign to top, the value of either left or right.
        top = left

        # Check for the edge case where the top is the target
        if mountain_arr.get(top) == target:
            return top

        # Now that we have the Top of the mountain's index, we will go down the mountain to find the target. We traverse the left side first, because the problem is looking for the first instance in the array.  If the target can be found on both sides, we will only need to find the ascending one.
        

        left = 0
        right = top
        median = (right + left) // 2

        #traverse the ascending part of the mountain
        while left < right:
            focus = mountain_arr.get(median)
            
            if focus == target:
                return median
            
            elif focus > target:
                right = median
                median = (right + left) // 2
            
            elif focus < target:
                left = median + 1
                median = (right + left) // 2

        # Check the edge case where the final index of left = right is where the target is.
        if mountain_arr.get(left) == target:
            return left

        # And now we traverse the descending side of the mountain

        left = top
        right = initial_right
        median = (right + left) // 2

        while left < right:
            focus = mountain_arr.get(median)
            
            if focus == target:
                return median
            
            elif focus > target:
                left = median + 1
                median = (right + left) // 2

            elif focus < target:
                right = median
                median = (right + left) // 2
        
        # Check the edge case where the final index of left = right is where the target is. 
        if mountain_arr.get(left) == target:
            return left

        # If we couldnt find our target traversing up or down, then it isnt in our array, and we return -1.
        
        return -1



myArray = MountainArray([4125,5630,8007,10771,14990,19595,22305,26733,28586,29853,30536,31819,32540,33502,36035,38424,38867,38896,43944,44517,48894,51974,57059,59058,63290,66687,71638,75519,80409,84118,85330,88729,93253,93791,94088,98088,101590,104571,109452,110031,112908,112958,115256,118432,123177,123937,125432,127298,128323,128573,130202,134601,137553,141452,144268,146616,147961,148626,149616,151814,154407,158938,161066,164052,166314,169783,172290,177175,180177,180304,185254,187733,182679,178999,178316,175489,171765,170704,168804,166744,166574,164900,163159,161952,157831,155461,153462,149464,148892,147158,142737,137649,133305,132410,131819,129158,126857,123521,121387,121190,116742,116453,111654,107589,104536,100859,97449,96165,95203,90561,88228,88047,85675,81633,77851,76618,72367,70989,68958,67280,62567,62059,61072,56874,56271,51957,49738,44878,41570,37222,36721,36362,34453,34397,33444,29117,27512,27078,25473,23894,21122,18820,14420,10194,6892,6474,2185,0]
)

Sol = Solution

array2 = MountainArray([0,1,2,4,2,1])
array3 = MountainArray([1,5,2])

print(Sol.findInMountainArray(Sol, 5, array3))