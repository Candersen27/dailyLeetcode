"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs

A pair (i, j) is called good if nums[i] = nums[j] and i < j


Strategy

I'm going to use combinitorics to find the total number of pairs in the array.
for each different number I can do c(n, 2) where n is the total number of a given value in the array.

Algorithm

First I'll create a dictionary.  The purpose of the dictionary will be to log every value in the array and give the associated total number of times the value appears.

Next I will iterated through the array.  If the number I see in the array isn't yet in the dictionary, I will add a key, and set its value to one.  If the number is already in the dictionary I will add one to its value.


Then I will create a variable called answer and set it to zero.  This will be the value I eventually return.

Finally I will iterate through the dictionary, and find c(n, 2) for the value associated with each key.  I will add that value to answer, and reassign to answer the result. At the end of the iteration I can return value and have my answer.


"""
# Import the math module so we can work with combinations
import math

class Solution:
    def numIdenticalPairs(self, nums):
        
        # Initialize a dictionary to hold information on the number of times each number in the nums array appears
        nums_dict = {}
        # Loop through the nums array.  If a value hasnt appeared yet, give it a key value pair and initialize the value as one.  If it has already appeared, find its key and add one to the value.
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            
            else:
                nums_dict[num] += 1
        # initialize the answer variable we will eventually return this value.
        answer = 0
        
        # iterate through the keys in nums_dict.  get the value associated with each key and find the value of c(n, 2) where n is the value.  Then add to answer and reassign the sum to answer's value.
        for key in nums_dict:
            value = nums_dict[key]
            combinations = math.comb(value, 2)
            answer += combinations
        
        # After we're finished, answer should hold the value of the number of pairs in the array.
    
        return answer
        





Sol = Solution
Q1 = [1, 2, 3, 1, 1, 3]
Q2 = [1, 1, 1, 1]
Q3 = [1, 2, 3]
Q4 = [1,3,2,4,5,1,2,3,2,2,2,2,3,4,1,5,6,7,1,4,7,1,2,3,3,3]



print(Sol.numIdenticalPairs(Sol, Q1))
print(Sol.numIdenticalPairs(Sol, Q2))
print(Sol.numIdenticalPairs(Sol, Q3))
print(Sol.numIdenticalPairs(Sol, Q4))