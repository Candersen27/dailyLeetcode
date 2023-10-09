"""
1458. Max Dot Product of Two Subsequences

Given Two Arrays nums1 and nums2.

Return the MAXIMUM dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of an array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.


Example 1:
    Input: nums1 = [2,1,-2,5]
           nums2 = [3, 0, -6]

    Output: 18

    Explanation:
        Take the subsequence [2, -2] from nums1 and subsequence [3, -6] from nums2.
        Their Dot product is  2*3  +  -2*-6 = 6 + 12 = 18

    Strategy:
        The best way to handle this problem is to create a table that records the maximum value for the two lists for any given length of the first n numbers in nums1 and nums2.

        That max value can be found by looking for the max of 4 values:
            a) take the value at the location on the table up one and to the left, and add it to the product of the last number in nums1 and the last number in nums2.
            b) take the value at the location directly to the left on the table
            c) take the value at the location directly above on the table
            d) the product of the last element of nums1 and nums2.
        
        enter this value for every element in the table.  The number at the bottom right should be the final max value.

        Note its important to load the table with an extra row and column as a buffer for empty subsequences.
"""



class Solution:
    def maxDotProduct(self, nums1, nums2):

        # First create a table that will eventually hold the maximum value for any given subsequences of length nums1 = i, nums2 = j, add one to each to show the case of an empty array.
        rows = len(nums1) + 1
        cols = len(nums2) + 1


        numsTable = [[float('-inf') for _ in range(cols)] for _ in range(rows)]

        # Iterate over the table with a nested for loop.
        for i in range(1, rows):
            for j in range(1, cols):

                """
                The value of any given element in the table will be the largest of one of four values:
                    a) take the value at numstable[i-1][j-1] and add it to the product of nums1[i] and nums2[j]
                    b) exclude nums1[i] from the subsequences and take the maximum dot product of subarrays ending at nums1[i-1] and nums2[j]
                    c) exclude nums2[j] from the subsequences and take the maximum dot product of subarrays ending at nums1[i] and nums2[j-1]
                    d) start a new subsequence from nums1[i] and nums2[j].  Their product is the maximum dot product.

                Obtain these four values and determine the max.  Input that value into the table at location [i][j]
                """
                #print(f"i: {i}, j: {j}, nums1[i-1]: {nums1[i-1]}, nums2[j-1]: {nums2[j-1]}")

                a = numsTable[i-1][j-1] + nums1[i-1]*nums2[j-1]
                b = numsTable[i-1][j]
                c = numsTable[i][j-1]
                d = nums1[i-1]*nums2[j-1]

                numsTable[i][j] = max(a,b,c,d)
                #print(f"max: {numsTable[i][j]}")
                #print(numsTable)

        # The value at numsTable[i][j] will be the maximum possible value, so we return that.
        return numsTable[rows-1][cols-1]



Sol = Solution
print(Sol.maxDotProduct(Sol, [2, 1, -2, 5], [3, 0, -6]))