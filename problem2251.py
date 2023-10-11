"""
Problem 2251: Number of Flowers in Full Bloom (Hard)

You are given a 0-indexed 2d integer array flowers, where flowers[i] =[start_i, end_i] means the ith flower will be in full bloom from start_i to end_i (inclusive).
You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Example: 1
    Input: flowers = [[1,6], [3,7], [9,12], [4,13]], people = [2,3,7,11]
    Output: [1,2,2,2]
    Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive. For each person, we return the number of flowers in full bloom during their arrival.

Example: 2
    Input: flowers = [[1,10],[3,3]], people = [3,3,2]
    Output: [2,2,1]
    Explanation: The figure aove shows the times when the flowers are in full bloom and when people arrive. For each person, we return the number of flowers in full bloom during their arrival.

Constraints:
    1 <= flowers.length <= 50,000
    flowers[i].length == 2
    1 <= start_i <= end_i <= 1,000,000,000
    1 <= people.length <= 50,000
    1 <= people[i] <= 1,000,000,000

    

Strategy:

This problem is made difficult by how large the constraints are.  The size of start_i and end_i as well as people_i can be up to a billion.  This rules out using something like a bucket_sort algorithm because the range of the sorting array will be too large.  When n is a billion, even O(n) wont work.  Similarly, an array size for people and flowers of fifty-thousand will make an algorithm with O(n^2) not viable as well.

Instead we can use a tree to store flowers that are in bloom, and iterate through both flowers and people concurrently.  This will allow us to keep O(n(log(n))).

First we want to sort flowers by bloom time (first element), and sort people.

Next we want to build a tree to put the flowers which are in bloom, and change flowers to a deque so we can pop elements from the left.

We want to iterate through the people array.
    For each person, we pop elements from the flowers deque where the bloom time is <= the visit time, until we hit a value that is larger.
    We take the wither time (second element) and insert them into our tree.
    Remove from the tree all elements with a value < the visit value.
    Count the total number of elements in the tree, and return that value to answer[i]

    

"""


class Solution:
    def fullBloomFlowers(self, flowers, people):
        pass