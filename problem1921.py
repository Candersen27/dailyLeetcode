"""
1921. Eliminate Maximum number of Monsters

You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed inter array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that can be eliminated before you lose, or n if you can eliminate all the monsters before they reach the city.

Example 1:
    Input: dist = [1,3,4], speed = [1,1,1]
    Output: 3
    Explanation:
        In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
        After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
        After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.
        All 3 monsters can be eliminated.

Example 2:
    Input: dist = [1,1,2,3], speed = [1,1,1,1]
    Output: 1
        Explanation:
        In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
        After a minute, the distances of the monsters are [X,0,1,2], so you lose.
        You can only eliminate 1 monster.


Constraints:

    n == dist.length == speed.length
    1 <= n <= 10^5
    1 <= dist[i], speed[i] <= 10^5


Strategy:
    In order to optimize our score, we need to know the correct order to blast the monsters.  One good way of figuring that out, would be to simulate a 'race' of the monsters, where each monster has to get to the finish line, (the city) and we record the order in which they get there. From here, we choose to blast the monsters in the order in which they would place in the race.

    Unfortunately the constraints make it unrealistic to run a race of large n sizes (10^5), instead we will calculate how many turns it would take each monster to reach the city, and can determine the placements from that information.

"""
import math

class Solution:
    def eliminateMaximum(self, dist, speed):

        # Initialize a turns array.  They will have -1 in every slot at first, but will soon change to more relevant data
        turns = [-1] * len(dist)

        # Change the value of each element in turns with the number of turns it would take each monster to reach the city. (dont forget to round up)
        for i in range(len(dist)):
            turns[i] = math.ceil(dist[i] / speed[i])
        
        # After sorting the turns we will have the order in which we want to shoot the monsters.  We will be treating this list like a stack, so we want to have the monsters that reach the city first be at the back of the list.
        turns = sorted(turns, reverse = True)

        # Now we play the game to see how high our score is
        score = 0
        print(turns)
        while True:
            
            turns.pop()
            print(turns)
            score += 1
            # Check to see if there are any elements left in the turns array, if not, we have shot all the monsters, and our score will reflect that.
            if not turns:
                return score
            
            # Checks to see if a monster reaches the city, ending our game. Because we always get one point per turn, score will always equal the number of turns we have taken.
            if turns[-1] <= score:
                return score
            
            


d = [10,20,30]
sp = [2, 3, 4]
Sol = Solution


print(Sol.eliminateMaximum(Sol, d, sp))