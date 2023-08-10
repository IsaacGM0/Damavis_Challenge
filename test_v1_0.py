#### All test functions ####

from aux_functions_v1_3 import *
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

def test_Valid_Right():
    for x in list(range(0,len(labyrinth_Valid_Moves1))):
        for y in list(range(0,len(labyrinth_Valid_Moves1[0])-2)):
            try:
                assert(Valid_Right(x,y,"horizontal",labyrinth_Valid_Moves1))   ## First we see in a labyrinth with full ".", so we can always move the rod without hit the wall
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the right from ({},{}). ".format(x,y)))
            
    for x in list(range(1,len(labyrinth_Valid_Moves1)-1)):
        for y in list(range(0,len(labyrinth_Valid_Moves1[0])-1)):
            try:
                assert(Valid_Right(x,y,"vertical",labyrinth_Valid_Moves1))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the right from ({},{}). ".format(x,y)))
    for x in list(range(0,len(labyrinth_Valid_Moves2))):                        ## Next, we  see in a labyrinth with full "#", so we can't move the rod
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Right(x,y,"horizontal",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the right when it mustn't move from ({},{}). ".format(x,y)))
    for x in list(range(0,len(labyrinth_Valid_Moves2))):                        
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Right(x,y,"vertical",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the right when it mustn't move ({},{}). ".format(x,y)))
            
### The following test_Valid_Moves are analogous

def test_Valid_Left():
    for x in list(range(0,len(labyrinth_Valid_Moves1))):
        for y in list(range(2,len(labyrinth_Valid_Moves1[0]))):
            try:
                assert(Valid_Left(x,y,"horizontal",labyrinth_Valid_Moves1))   
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the left from ({},{}). ".format(x,y)))
            
    for x in list(range(1,len(labyrinth_Valid_Moves1)-1)):
        for y in list(range(1,len(labyrinth_Valid_Moves1[0]))):
            try:
                assert(Valid_Left(x,y,"vertical",labyrinth_Valid_Moves1))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the left from ({},{}). ".format(x,y))) 

    for x in list(range(0,len(labyrinth_Valid_Moves2))):                     
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Left(x,y,"horizontal",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the left when it mustn't move from ({},{}). ".format(x,y))) 
    for x in list(range(0,len(labyrinth_Valid_Moves2))):                       
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Left(x,y,"vertical",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the left when it mustn't move ({},{}). ".format(x,y)))


def test_Valid_Up():
    for x in list(range(1,len(labyrinth_Valid_Moves1))):
        for y in list(range(1,len(labyrinth_Valid_Moves1[0])-1)):
            try:
                assert(Valid_Up(x,y,"horizontal",labyrinth_Valid_Moves1))   
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the up from ({},{}). ".format(x,y)))
            
    for x in list(range(2,len(labyrinth_Valid_Moves1)-1)):
        for y in list(range(0,len(labyrinth_Valid_Moves1[0]))):
            try:
                assert(Valid_Up(x,y,"vertical",labyrinth_Valid_Moves1))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the up from ({},{}). ".format(x,y))) 

    for x in list(range(0,len(labyrinth_Valid_Moves2))):                     
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Up(x,y,"horizontal",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the up when it mustn't move from ({},{}). ".format(x,y))) 
    for x in list(range(0,len(labyrinth_Valid_Moves2))):                       
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Up(x,y,"vertical",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the up when it mustn't move ({},{}). ".format(x,y)))
            
def test_Valid_Down():
    for x in list(range(0,len(labyrinth_Valid_Moves1)-1)):
        for y in list(range(1,len(labyrinth_Valid_Moves1[0])-1)):
            try:
                assert(Valid_Down(x,y,"horizontal",labyrinth_Valid_Moves1))   
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the down from ({},{}). ".format(x,y)))
            
    for x in list(range(1,len(labyrinth_Valid_Moves1)-2)):
        for y in list(range(0,len(labyrinth_Valid_Moves1[0]))):
            try:
                assert(Valid_Down(x,y,"vertical",labyrinth_Valid_Moves1))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the down from ({},{}). ".format(x,y))) 

    for x in list(range(0,len(labyrinth_Valid_Moves2))):                     
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Down(x,y,"horizontal",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the down when it mustn't move from ({},{}). ".format(x,y))) 
    for x in list(range(0,len(labyrinth_Valid_Moves2))):                       
        for y in list(range(0,len(labyrinth_Valid_Moves2[0]))):
            try:
                assert(not Valid_Down(x,y,"vertical",labyrinth_Valid_Moves2))
            except AssertionError :
                raise( AssertionError("Error trying to move the rod to the down when it mustn't move ({},{}). ".format(x,y)))


### It is not necessary a test for Valid_Rotation, it just depends on the other Valid_Moves and the same for Neighbors.

a= Find_Neighbors(1,2,"vertical",labyrinth)
for i in a:
    print(i.x,i.y,i.orientation)

test_Valid_Labyrinth_Range()
test_Valid_Labyrinth_Symbols()
test_Valid_Right()
test_Valid_Left()
test_Valid_Up()
test_Valid_Down()

