# Countdown Numbers Game Solver

Countdown is a British game show that tests the contestants' knowledge of numbers and words. 

This is a simple script made to solve any given permutation of the **Countdown Numbers Game**. 

For those unfamiliar, this game is played [as such](https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round): 
1. 6 numbers are chosen at random. These numbers are either from 1-10 (small numbers) or 25, 50, 75 or 100 (big numbers)
2. A 3-digit "target" number is generated at random
3. Contestants have 30 seconds to use only the 4 basic mathematical operations `(+ - * /)` and the 6 numbers to solve for the target number.

On the show, they have the beautiful and talented Rachel Riley to come up with the solution on the spot to check against the contestants' solutions. But I'm nowhere near as good
at math as her so I figured I'd try to write a script to do it for me. 

## Known Issues:
- Only finds 1 solution
- Solution might not be the shortest
- Technically fractions are not allowed in the game, but the script might use fractions in the solution. 
It should, however, be trivial for a human to rearrange the generated solution to not use fractions. 
- Does not take advantage of the limited number pool. But this might also be an advantage because that means it can be used for numbers outside of the number pool
