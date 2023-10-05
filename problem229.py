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
    def majorityElement(self, nums):
        
        # Initialize variables
        nums_dict = {}
        answer = []

        # Loop through the nums array, If a value hasnt yet appeared, give it a key value pair and initialize the value as one. If it has already appeared, find its key and add one to the value.
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            
            else:
                nums_dict[num] += 1

        # Loop through the entries in the nums_dict dictionary.  for each value, if it is larger than one third the length of the nums array, then we want to return the key as part of our answer.
        for key in nums_dict:
            value = nums_dict[key]

            if value > (len(nums)/3):
                answer.append(key)
        
        return answer
    

Sol = Solution

Q1 = [3, 2, 3]
Q2 = [1]
Q3 = [1, 2]
Q4 = [2, 2, 8, 8, 1, 1, 1, 1, 8, 8]


print(Sol.majorityElement(Sol, Q1))
print(Sol.majorityElement(Sol, Q2))
print(Sol.majorityElement(Sol, Q3))
print(Sol.majorityElement(Sol, Q4))
