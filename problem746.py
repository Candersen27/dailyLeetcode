"""
Problem 746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.  Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0 or index 1.

Return the minimum cost to reach the top of the floor.

Example 1.

    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: You will start at index 1.
        - Pay 15 and climb two steps to reach the top. 
        The total cost is 15.

Example 2.

    Input: cost = [1,100,1,1,1,100,1,1,100,1] 
    Output: 6
    Explanation: You will start at index 0.
        - Pay 1 and climb two steps to reach index 2.
        - Pay 1 and climb two steps to reach index 4.
        - Pay 1 and climb two steps to reach index 6.
        - Pay 1 and climb one step to reach index 7.
        - Pay 1 and climb two steps to reach index 9.
        - Pay 1 and climb one step to reach the top.
        The total cost is 6.


Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999


    Strategy:
        This is a simple dynamic programming problem.  The idea is to reach the top of the stairs/end of the array with the minimum cost.
        To do this we will create an empty array called dp.  The value at any index dp[i] should be the total minimum cost it would take to reach the associated index at cost[i]

        We can start out by initializing dp[0] and dp[1], because those costs will obviously be equal to their associated indicies in cost
            (dp[0] = cost[0], dp[1] = cost[1])

        From here on, we calculate the minimum cost to reach that step.  The value of any dp[i] will be equal to the cost asociated with landing on dp[i] + the minimum of the cost associated with landing on the lower of the two previous steps.
            (dp[i] = cost[i] + min(dp[i-1], dp[i-2]))

        We dynamically fill out the dp array, and our final answer will be the lower of the final two elements in dp)
"""
class Solution:
    def minCostClimbingStairs(self, cost):
        
        # Set n to be the length of the cost array and use it to initialize our dp array.
        n = len(cost)
        dp = [0 for _ in range(len(cost))]
        
        # Initialize the first two elements in dp
        dp[0] = cost[0]
        dp[1] = cost[1]

        # loop through the rest of dp
        for i in range(2, n):
            # The value of the total cost to reach a given step is the value of that step plus the lower of the two previous total costs
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])

        # The lower total cost between the final two steps is our answer
        return int(min(dp[n-2], dp[n-1]))
    


Sol = Solution

Q1 = [10, 15, 20]
Q2 = [1,100,1,1,1,100,1,1,100,1]

print(Sol.minCostClimbingStairs(Sol, Q1))
print(Sol.minCostClimbingStairs(Sol, Q2))
