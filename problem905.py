"""
905. Sort Array by Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.



Example 1:
    Input: nums = [3, 1, 2, 4]
    Output: [2, 4, 3, 1]

"""

class Solution:
    def sortArrayByParity(self, nums):

        answer = []
        

        for num in nums:
            if num % 2 == 0:
                answer.insert(0, num)
            else:
                answer.append(num)
        
        
        return answer
    


S = Solution

input = [3,4,2,1,5,8,3]
answer = S.sortArrayByParity(S, input)
print(answer)

