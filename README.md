# Damavis_Challenge

## Abstract

The goal is to carry the rod from the top left corner of the labyrinth to the bottom
right corner. This rod is not exactly the lightest thing you can imagine, so the
participant would naturally want to do it as fast as possible.
Find the minimal number of moves required to carry the rod through the labyrinth.
The labyrinth can be represented as a rectangular matrix, some cells of which are
marked as blocked, and the rod can be represented as a 1 × 3 rectangle. The rod
can't collide with the blocked cells or the walls, so it's impossible to move it into a
position in which one of its cells coincides with the blocked cell or the wall. The goal
is thus to move the rod into position in which one of its cells is in the bottom right
cell of the labyrinth.
There are 5 types of moves that the participant can perform: move the rod one cell
down or up, to the right or to the left, or to change its orientation from vertical to
horizontal and vice versa. The rod can only be rotated about its center, and only if the
3 × 3 area surrounding it is clear from the obstacles or the walls.
The rod is initially positioned horizontally, and its left cell lies in [0, 0].

Here an example:

![Image_Rod](https://github.com/IsaacGM0/Damavis_Challenge/assets/106811614/421fac53-4376-4cdf-91df-8ae5aff81652)

## Resolution

First of all, we have to define the reference system:

![Perspectiva](https://github.com/IsaacGM0/Damavis_Challenge/assets/106811614/9e44fc53-bab8-484c-89c9-7b09531732bb)


Now that we have the reference system, a matrix (which is the labyrinth) of dimensions (m,n), and by the given indications we
we can start with the rod occupying (0,0),(0,1),(0,2) or (0,0),(1,0),(2,0) and we need to end at the
(m-1,n-3),(m-1,n-2),(m-1,n-3) or (m-3,n-1),(m-2,n-1), (m-1,n-1).

For example, in the previous image we have a labyrinth with dimensions (5,9), the rod starts at (0,0),(0,1),(0,2) and ends
in the (5-3,9-1),(5-2,9-1),(5-1,9-1)=(2,8),(3,8),(4,8).


Now we have all the ingredients, a referemce system, a matrix, an object, which is in the matrix, that we must move.
The objective is find the shortest path for that object (rod), so we can use an algorithm for this. In this case I have used the
A* algorithm. To see an example of this I recommend reading David Martín's article 
<https://blog.damavis.com/grafos-encontrando-caminos-optimos/> and for more details about this algorithm
<https://en.wikipedia.org/wiki/A*_search_algorithm>.

## Files

You can solve this problem downloading the next files:

- main_v2_0
- aux_functions_v2.0
- examples

### INPUT

You must introduce as input a rectangular matrix with "." and "#". Like this:
  
![Labyrinth](https://github.com/IsaacGM0/Damavis_Challenge/assets/106811614/dfe2c511-bbb4-470f-bd3c-9c37c1241e8c)

The matrix dimensions must be between 3 and 1000.

### OUTPUT

result : It is an integer, and it is the number of moves required to carry the rod to the end of labyrinth or -1 if it is
impossible.

You can activate "print(f"({x}, {y})")" in main_v2_0.py if you want to see the path from the start to the end.


### Other files

- test_main

  Here I have applied the algorithm to tests of the challenge.

- test_v2_0
- examples_test

  Here are the tests of auxiliary functions and the labyrinths that I used to test it. 



## IDEAS

It would be interesting to formulate this problem in linear programming to obtain more tests for the script and to have some 
certainty if this is well programmed.

It would also be interesting to carry out this problem with a rod of (m,n) dimensions or with the possibility that the rod could move diagonally.

