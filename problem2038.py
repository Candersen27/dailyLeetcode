"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color

There are n pieces arranged in a line, and each piece is colored by either 'A' or 'B'. You are given a string COLORS of length n where COLORS[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

    - Alice is only allowed to remove an 'A' piece if both its neighbors are also colored 'A'. She is not allowed to remove pieces colored 'B'.

    - Bob is only allowed to remove a 'B' piece if both its neighbors are also colored 'B'. She is not allowed to remove pieces colored 'A'.

    - Alice and Bob cannot remove pieces from the edge of the line.

    - If a player cannot make a move on their turn, that plater loses, and the other player wins.

Assuming Alice and Bob play optimally, return True if Alice wins, or return False if Bob wins.



Okay, so 'play optimally' is a McGuffan, any legal move for either player will be as good as playing optimally.

We should be able to shortcut who wins the game by understanding that it is non-interactive.  No matter what one player does with their move, it will be impossible to disrupt the number of turns the other player will have to survive.

In fact we can determine for both players how long they will be able to remove pieces before they can not anymore and will lose. Therefore instead of treating this like a game and building turns with a while loop.  

We can just count up the number of turns each player has to survive.  Whoever has the higher number will be the winner.  Because Alice moves first, she will lose any tie-breakers.


First we want to turn the string into a list of characters.

Then we initialize variables for both alice and bob's scores.  These values will start at zero and as we iterate through the list of characters, will represent the number of turns bob and alice will have before they lose.

At the end of the iteration we will be able to know who will last the longest and we can declare them the winner by returning either True or False.

"""


class Solution:
    def winnerOfGame(self, colors):
        
        # Change the colors string into a list of characters, and initialize bob and alices scores.
        colors_list = list(colors)
        a_score = 0
        b_score = 0

        # Initialize a streak variable.  This will keep track of how many characters in a row are the same.  We start at 1 because the first character in the list will count itself.
        streak = 1
        for i in range(1, len(colors_list)):
            # If the streak continues add one to the value of streak and move on to the next character
            if colors_list[i] == colors_list[i - 1]:
                streak += 1
            
            # If the streak breaks, we use the streak variable to determine how many points to give which player.
            else:
                # We only want to give players points if we get streaks of 3 or more.
                # For example 'AAAAA' will let alice survive for 3 turns, so that would pass the if statement and we add 3 to her score
                if colors_list[i-1] == 'A' and streak > 2:
                    a_score += streak - 2
                
                elif colors_list[i-1] == 'B' and streak > 2:
                    b_score += streak - 2

                # Reset the streak with colors_list[i] being the beginning of the new streak
                streak = 1
        
        # After iterating though the list, we run a final if elif block to give points to a player for the last streak.
        if colors_list[i] == 'A' and streak > 2:
            a_score += streak - 2
                
        elif colors_list[i] == 'B' and streak > 2:
            b_score += streak - 2

        



        print(a_score)
        print(b_score)

        if a_score > b_score:
            return True
        
        else:
            return False
        


Sol = Solution
colors = 'AAAABBBB'


r = Sol.winnerOfGame(Sol, colors)
print(r)