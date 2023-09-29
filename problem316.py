"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""







class Solution(object):
    def removeDuplicateLetters(self, s):

        list_s = list(s)
        copy_list_s = list(s)
        stack = []

        for element in list_s:
            copy_list_s.pop(0)
            if element not in stack:
                while stack and stack[-1] > element and stack[-1] in copy_list_s:
                    stack.pop()
                stack.append(element)
                print(stack)
        stack_string = ''.join(stack)
        return stack_string
    


Sol = Solution
my_string = "cbacdcbc"
answer = Sol.removeDuplicateLetters(Sol, my_string)
print(answer)

my_string2 = "bcabc"
answer2 = Sol.removeDuplicateLetters(Sol, my_string2)
print(answer2)

"""
bcabc
[b,c,a,b,c]
[c,a,b,c]   [c]
"""


