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

"""


class Solution:
    def winnerOfGame(self, colors):
        print('Under Construction')