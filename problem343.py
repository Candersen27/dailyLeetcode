"""
343. Integer Break

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximaize the product of those integers.

Return the maximum product you can get

Example 1:
    Input: n = 2
    Output: 1
    Explanation: 2 = 1 + 1, 1 x 1 = 1

Example 2:
    Input: n = 10
    Output: 36
    Explanation: 10 = 3 + 3 + 4, 3 x 3 x 4 = 36

    

Strategy:
    The trick to this problem is figuring out what causes the optimization.  To find out I looked at brute forcing a sample n, and found where the peak was for all k. To get the optimization for any k, given an n, we can divide n by k, and round down, that number will be the value to initially put in for all the numbers to be multiplied (m). if there is a modulo, add on to that many of the m. 

    As I sifted through the answers I got, I realized that the output kept growing until it hit a number as close to 3^(n/3) as it could.  This will allow me to create an algorithm that finds that value and returns it instead of brute forcing an answer.

    I also realized that the algorithm didn't work for n < 10. If I found n to be 10 or less, I just found the answer by brute force.  For values that small it wouldnt be a significant issue in proccessing.
"""

class Solution:
    def integerBreak(self, n):
        

        small_n_list = {
            1: 1,
            2: 1,
            3: 2,
            4: 4,
            5: 6,
            6: 9,
            7: 12,
            8: 18
            
        }
        # This algorithm will work for n > 10, for 1 <= n <= 8 it will be most efficient to just hard code the answers.
        if n > 8:
            answer = 1

            while n > 4:
                n = n - 3
                answer = answer * 3
            
            answer = answer * n

            return answer
        
        else:
            return small_n_list[n]
    

Sol = Solution

Q0 = 5
Q1 = 15
Q2 = 48

print(Sol.integerBreak(Sol, Q1))
print(Sol.integerBreak(Sol, Q2))
print(Sol.integerBreak(Sol, Q0))



