"""
557. Reverse Words in a String

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1: 
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    
Algorithm

First i want to break down the entire phrase into a list of characters

Then I will iterate through the list.  I will check to see if the character is a space ' '.  If it is not, I will concatenate it to the end of a word variable.  If it is, that means its the end of the word, and I will reverse the order of my word variables characters using the slice [::-1], and I will assign the reversed word to a list called answer.  After this I will reset the word variable to '', and keep going through the loop.

I will keep doing this in the for loop until I hit the end.  My last word will not have a space at the end, but I still want to add it to the list.  After my for loop ends my word variable will still hold all the correct characters i need, so i will simply use the reverse slice, append the word to answer, and reset word, just like if it were to hit the if/else appropriately.

finally, I will concatenate each word in the answer list, to a finalAnswer variable with an additional space at the end.  This will give me a string almost exactly what I'm looking for, except for an extra space at the end.  Using the strip() command will clean this up, and I will finally return the result.
"""


class Solution:
    def reverseWords(self, s):
        
        # Initialize variables.  answer_list will be a list of words that I put in my final string.  word will be a string that we add characters to to create our words.  final_answer will be the concatenation of the words in answer_list
        answer_list = []
        word = ''
        final_answer = ''
        
        # Turn the input into a list of characters
        s_list = list(s)

        # Run a for loop that checks every character in list_s
        for char in s_list:     # If the character isnt a space add the letter to the end of our word.
            if char != ' ':
                word = word + char

            else:   # We hit a space
                # This slice will reverse the order of the letters in our word
                # Add the word to the end of the answer list, and reset the word variable
                word = word[::-1]
                answer_list.append(word)
                word = ''
        
        # Now that we're out of the for loop, we still need to add the last word to the list.
        word = word[::-1]
        answer_list.append(word)
        word = ''

        # Concatenate the reversed words in our answer list together along with spaces.
        for reversedWord in answer_list:
            final_answer = final_answer + reversedWord + ' '
        
        # Trim the excess whitespace at the end of finalAnswer, and return the result.
        final_answer = final_answer.strip()
        return final_answer




Sol = Solution()
inputWord = "There's never enough cookies in the cookie jar!"
final = Sol.reverseWords(inputWord)

print(final)