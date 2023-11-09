"""
1759. Count number of Homogenous Substrings

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 10^9 + 7

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "abbcccaa"
    Output: 13
    Explanation: The homogenous substrings are listed below.
        'a' appears 3 times
        'aa' appears 1 time
        'b' appears 2 times
        'bb' appears 1 time
        'c' appears 3 times
        'cc' appears 2 times
        'ccc' appears 1 time

        3 + 1 + 2 + 1 + 3 + 2 + 1 = 13
    
        
Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase letters

"""


class Solution:
    def countHomogenous(self, s):
        
        # Initialize count and answer variables.  Answer will eventually be the return value.  Count will count the given length of a homogenous substring of s, and will be reset often
        count = 1
        answer = 0
        for i in range(1, len(s)+ 1):
            
            # Check to see if we reached the end of the string. If so add the final substring and return the answer.
            if i > len(s) - 1:
                tnf = (count * (count + 1)) // 2
                answer += tnf
                return answer % (10 ** 9 + 7)

            if s[i] == s[i-1]:
                count += 1
                
            else:
                # The formula (k×(k+1))/2 represents the sum of the first k natural numbers, also known as the triangular Number formula.  This equation will give us the total number of substrings in a homogenous string of length k.
                tnf = (count * (count + 1)) // 2
                answer += tnf
                # because the value of the string changes, we reset the count
                count = 1

        return answer % (10 ** 9 + 7)
    

Sol = Solution

Q1 = "abbcccaa"
print(Sol.countHomogenous(Sol, Q1))