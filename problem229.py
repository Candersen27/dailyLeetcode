"""
229. Majority Element II

Given an array of size n, find all elements that appear more than [n/3] times

Example 1:
    Input: nums = [3, 2, 3]
    Output: [3]

Example 2:
    Input: nums = [1]
    Output: [1]

Example 3:
    Input: nums = [1, 2]
    Output: [1, 2]



Strategy:
    I want to use a dictionary to keep track of all the elements in nums along with the frequency I see each value in the list.
   
    After taking an inventory of every element in nums, I will go through the dictionary, and for each key value pair, if the value stored is larger than [n/3] where n is the size of the nums array, I will append the key to a new array called answer.

    Finally I will return the answer array 
"""

class Solution:
    def majorityElement(self, nums)
        pass

