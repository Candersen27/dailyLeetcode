"""
Given an array 'arr' of distinct integers and an integer k:

A game will be played between the first two elements of the array (arr[0] and arr[1]). In each round of the game, we compare arr[0] to arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.


Example 1:

    Input: arr = [2,1,3,5,4,6,7], k = 2
    Output: 5
    Explanation:
        Round   |   arr             |   winner  | win_count
        1       | [2,1,3,5,4,6,7]   |   2       |   1
        2       |   [2,3,5,4,6,7,1] | 3         | 1
        3       | [3,5,4,6,7,1,2]   | 5         | 1
        4       | [5,4,6,7,1,2,3]   | 5         | 2

        
Constraints:
    2 <= arr.length <= 10^5
    1 <= arr[i] <= 10^6
    arr contains distinct integers
    1 <= k <= 10^9
"""


class Solution:
    def getWinner(self, arr, k):
        
        n = len(arr)
        
        if k > n:
            return max(arr)
        
        # check to see if the initial element would win the game
        temp_arr = arr[:k+1]

        # hold a sliding value for the max element, so we don't need to recalculate the max value of an array slice over and over
        temp_max = max(temp_arr)

        if arr[0] == temp_max:
            return arr[0]
        
        
        for i in range(1, n - k):
            temp_arr = arr[i-1:i+k]
            # check to see if the new element introduced to the window is larger than the old window's max, if so, update temp_max. (we wont get a winner here because the new element is the new max)
            if temp_arr[-1] > temp_max:
                temp_max = temp_arr[-1]

            elif arr[i] == temp_max:
                return arr[i]
        
        return max(arr)



sol = Solution()

test_case_1 = ([2, 1, 3, 5, 4, 6, 7], 2)
test_case_2 = ([3, 2, 1], 10)
test_case_3 = ([5, 4, 3, 2, 1], 2)
test_case_4 = ([1, 2, 3, 4, 5], 3)
test_case_5 = ([-1, -2, -3, -4, -5], 3)
test_case_6 = ([1, 1, 1, 1, 1, 1], 4)
test_case_7 = ([10, 9, 8, 7, 6, 5], 2)
test_case_8 = ([5, 6, 7, 8, 9, 10], 4)
test_case_9 = ([3, 1, 5, 2, 4], 3)

res_1 = sol.getWinner(*test_case_1)
res_2 = sol.getWinner(*test_case_2)
res_3 = sol.getWinner(*test_case_3)
res_4 = sol.getWinner(*test_case_4)
res_5 = sol.getWinner(*test_case_5)
res_6 = sol.getWinner(*test_case_6)
res_7 = sol.getWinner(*test_case_7)
res_8 = sol.getWinner(*test_case_8)
res_9 = sol.getWinner(*test_case_9)






print(f'Result of test case 1: {res_1}')
print(f'Result of test case 2: {res_2}')
print(f'Result of test case 3: {res_3}')
print(f'Result of test case 4: {res_4}')
print(f'Result of test case 5: {res_5}')
print(f'Result of test case 6: {res_6}')
print(f'Result of test case 7: {res_7}')
print(f'Result of test case 8: {res_8}')
print(f'Result of test case 9: {res_9}')