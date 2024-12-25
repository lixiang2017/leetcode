'''
https://www.reddit.com/r/adventofcode/comments/1hj2odw/2024_day_21_solutions/?sort=confidence

Boojum
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
[LANGUAGE: Python] 2578/1629

Eeeyuuuup. That's a late-AOC weekend puzzle. This one kind of melted my brain with all the levels to track. But I've gotta give credit, it nicely combines a lot of classic AOC elements.

The key observations that I found are:

The downstream bots (away from the numeric pad) always have to return to the A button. This effectively resets their position, so we can chunk the solve.

For any two buttons on a pad, there's a specific shortest path that is always best with respect to the downstream bots.

    - First, always prefer the path with the fewest turns. For going from 9 to 1 on the numeric pad, for example, prefer <<vv to something like <v<v. The path length at this level is the same, but it incurs extra movement for the downstream bots.

    - All else being the same, prioritize moving < over ^ over v over >. I found this through trial and error.

    - Given the existence of an always optimal route, we don't need to try different paths DFS style.

My original code for Part 1 originally made sequential passes over the string, term-rewriting style, scanning for pairs of moves and rewriting them into the instructions for the next downstream bot. That worked for Part 1, however the length of the string quickly gets quite huge in Part 2. So for Part 2, I rewrote it the usual memoized recursive sum and solve thing.

Here's my final code for Part 2 after cleaning it up. Change the 25 to 2 for the Part 1 solution.
'''

import fileinput, functools

n = [ "789", "456", "123", " 0A" ]
d = [ " ^A", "<v>" ]

def path( p, f, t ):
    fx, fy = next( ( x, y ) for y, r in enumerate( p ) for x, c in enumerate( r ) if c == f )
    tx, ty = next( ( x, y ) for y, r in enumerate( p ) for x, c in enumerate( r ) if c == t )
    def g( x, y, s ):
        if ( x, y ) == ( tx, ty ):            yield s + 'A'
        if tx < x and p[ y ][ x - 1 ] != ' ': yield from g( x - 1, y, s + '<' )
        if ty < y and p[ y - 1 ][ x ] != ' ': yield from g( x, y - 1, s + '^' )
        if ty > y and p[ y + 1 ][ x ] != ' ': yield from g( x, y + 1, s + 'v' )
        if tx > x and p[ y ][ x + 1 ] != ' ': yield from g( x + 1, y, s + '>' )
    return min( g( fx, fy, "" ),
                key = lambda p: sum( a != b for a, b in zip( p, p[ 1 : ] ) ) )

@functools.cache
def solve( s, l ):
    if l > 25: return len( s )
    return sum( solve( path( d if l else n, f, t ), l + 1 ) for f, t in zip( 'A' + s, s ) )

print( sum( solve( s.strip(), 0 ) * int( s[ : 3 ] )
            for s in fileinput.input() ) )

# run it
# python adventofcode/2024/day21/part2/greedy.py < adventofcode/2024/day21/part2/input
# 205620604017764