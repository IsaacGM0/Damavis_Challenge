#### All test functions ####

from aux_functions_v1_2 import *
from examples_test import *
#### Examples we are going to use to Valid_Labyrinth ####

labyrinth = [
    [".",".",".",".",".",".",".","."],
    [".","#",".",".",".",".","#","."],
    [".","#",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".","#",".",".",".",".",".","."],
    [".","#",".",".",".","#",".","."]
    ]

def test_Valid_Labyrinth_Range ():
    assert(Valid_Labyrinth_Range(labyrinth)== True )
    assert(Valid_Labyrinth_Range(labyrinth_Valid_Range1) == False)
    assert(Valid_Labyrinth_Range(labyrinth_Valid_Range2) == False)

def test_Valid_Labyrinth_Symbols ():
    assert(Valid_Labyrinth_Symbols(labyrinth)== True )
    assert(Valid_Labyrinth_Symbols(labyrinth_Valid_Symbols1) == False)
    assert(Valid_Labyrinth_Symbols(labyrinth_Valid_Symbols2) == False)


print(Valid_Labyrinth_Range(labyrinth_Valid_Range1) )
test_Valid_Labyrinth_Range()
test_Valid_Labyrinth_Symbols()
