"""
880. Decoded String at Index


You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.


Example 1:

Input:
s = "leet2code3", k = 10

decoded string is: "leetleetcodeleetleetcodeleetleetcode"

Example 2:

Input:
s = "ha22" k = 5

decoded string is: "hahahaha"
5th letter is h


first turn it into a list
[l, e, e, t, 2, c, o, d, e, 3]


"""


class Solution(object):
    def decodeAtIndex(self, s):
        """
        :type s: str
        :type l: list
        :type k: int
        :rtype: str
        """

        
        list_s = []
        list_answer = []
        list_temp = []
        # break the string up into characters and put them into a list.  
        # make sure to classify the numbers as ints and the letters as strings
        for char in s:
            if char.isdigit():
                list_s.append(int(char))
            else:
                list_s.append(char)
        
        for char in list_s:
            if isinstance(char, str):
                list_temp.append(char)
                list_answer.append(char)
                print(f'list temp: {list_temp}')
                print(f'list answer: {list_answer}')

            elif isinstance(char, int):
                print('number triggered')
                list_temp = list_answer.copy()
                for i in range(char - 1):
                    for char_temp in list_temp:
                        list_answer.append(char_temp)
                        print(f'list answer: {list_answer}')
            
        answer = ''.join(str(e) for e in list_answer)
        return list_answer



Sol = Solution()
code = "leet2code3"
answer = Sol.decodeAtIndex(code)
print(answer)

code2 = "ha22"
answer2 = Sol.decodeAtIndex(code2)
print(answer2)