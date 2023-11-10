"""
1743. Restore the Array from Adjacent Pairs

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [u_i, v_i] indicates that the elements u_i and v_i are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

Example 1:
    Input:  adjacent pairs = [[2,1],[3,4],[3,2]]
    Output: [1,2,3,4]
    Explanation: This array has all its adjacent pairs in adjacentPairs.
    Notice that adjacentPairs[i] may not be in left-to-right order.


Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 10^5
-10^5 <= nums[i], ui, vi <= 10^5
There exists some nums that has adjacentPairs as its pairs.
"""


class Solution:
    def restoreArray(self, adjacentPairs):
        
        
        find_start_dict = {}
        
        for tuple in adjacentPairs:
            u, v = tuple

            if u not in find_start_dict:
                find_start_dict[u] = 1

            else:
                find_start_dict[u] += 1
            
            if v not in find_start_dict:
                find_start_dict[v] = 1

            else:
                find_start_dict[v] += 1
            
        ticker = 0
        for entry in find_start_dict:
            if find_start_dict[entry] == 1:
                ticker += 1
                if ticker == 1:
                    start = entry
                else:
                    finish = entry
                    break

        
        adjacent_pairs_dict = {}

        for tuple in adjacentPairs:
            u, v = tuple

            if u not in adjacent_pairs_dict:
                adjacent_pairs_dict[u] = [v]
            else:
                adjacent_pairs_dict[u].append(v)

            if v not in adjacent_pairs_dict:
                adjacent_pairs_dict[v] = [u]
            else:
                adjacent_pairs_dict[v].append(u)

        print(f"dict: {adjacent_pairs_dict}")


        # This part of the code starts adding elements to the answer.  Start by adding the value at start, which we already determined was our first element in our answer
        answer = [start]
        active_number = start
        
        # This loop will last as long as the length of the value entry is greater than zero
        while active_number in adjacent_pairs_dict:
            next_candidates = adjacent_pairs_dict[active_number]

            # Choose the next element based on the number of candidates
            if len(next_candidates) == 1:
                next_number = next_candidates[0]
            else:
                # Choose the next element based on the one that is different from the previous number
                next_number = next_candidates[0] if next_candidates[0] != previous_number else next_candidates[1]

            answer.append(next_number)
            
            previous_number = active_number
            active_number = next_number

            if active_number == finish:
                break

        return answer

sol = Solution


q1 = [[1,2],[3,2],[3,4],[5,4]]
q2 = [[1,2],[5,4],[3,2],[3,4]]

print(sol.restoreArray(sol, q1))
print(sol.restoreArray(sol, q2))