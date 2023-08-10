#### Here are all auxiliar functions ####

def Valid_Labyrinth_Range(labyrinth): #Valid that the matrix has the dimensions (X,Y) where 3<=X,Y<=1000.

    if (3 > len(labyrinth) | len(labyrinth)>1000):
        return False
    len_labyrinth=len(labyrinth[0]) #Check if the matrix is ​​rectangular.
    for i in labyrinth:
        if(3 > len(i) or len(i)>1000 or len_labyrinth != len(i)):
            return False
    return True

def Valid_Labyrinth_Symbols(labyrinth): #Checks if the matrix only has "." and "#".
    for i in labyrinth:
        for j in i:
            if not  (j == "#" or  j == "." ):
                return False     
    return True

### All Valid_Move check if the rod can perform that move (Right, left, up, down or rotation) ###  
### It is necessary to differentiate if the rod is horizontal or vertical to check the walls and obstacles. ###
def Valid_Right(x,y,orientation,labyrinth):
    if (orientation == "vertical" and len(labyrinth[0])>y+1 and x>0 and x+1<len(labyrinth)): #x>0 is necessary, our rod can't walk through walls (analogous for the rest moves).
        return labyrinth[x-1][y+1] == labyrinth[x][y+1] == labyrinth[x+1][y+1] == "." 
    if (orientation == "horizontal" and len(labyrinth[0])>y+2):
        return labyrinth[x][y+2] == "." 
    return False

def Valid_Left(x,y,orientation,labyrinth): 
    if (orientation == "vertical" and 0<y and x>0 and x+1<len(labyrinth)):
        return labyrinth[x-1][y-1] == labyrinth[x][y-1] == labyrinth[x+1][y-1] == "." 
    if (orientation == "horizontal" and 0<y-1):
        return labyrinth[x][y-2] == "." 
    return False

def Valid_Up(x,y,orientation,labyrinth): 
    if (orientation == "vertical" and 0<x-1):
        return labyrinth[x-2][y] == "." 
    if (orientation == "horizontal" and 0<x and y>0 and y+1<len(labyrinth[0])):
        return labyrinth[x-1][y-1] == labyrinth[x-1][y] == labyrinth[x-1][y+1] == "." 
    return False

def Valid_Down(x,y,orientation,labyrinth): 
    if (orientation == "vertical" and len(labyrinth)>x+2):
        return labyrinth[x+2][y] == "." 
    if (orientation == "horizontal" and len(labyrinth)>x+1 and y>0 and y+1<len(labyrinth[0])):
        return labyrinth[x+1][y-1] == labyrinth[x+1][y] == labyrinth[x+1][y+1] == "." 
    return False

def Valid_Rotation(x,y,orientation,labyrinth):
    if(orientation == "vertical"):
        if(Valid_Right(x,y,"vertical",labyrinth) and Valid_Left(x,y,"vertical",labyrinth)): #If being vertical, we can move horizontally, we can rotate.
            return True
    if(orientation == "horizontal"):
        if(Valid_Up(x,y,"horizontal",labyrinth) and Valid_Down(x,y,"horizontal",labyrinth)): #If being horizontal, we can move vertically, we can rotate.
            return True
    return False


def Find_Neighbors(x,y,orientation,labyrinth): #Check all the paths we can follow with the rod.
    neighbors=[]
    if(Valid_Right(x,y,orientation,labyrinth)):
        neighbors.append(Node(x,y+1,orientation))
    if(Valid_Left(x,y,orientation,labyrinth)):
        neighbors.append(Node(x,y-1,orientation))
    if(Valid_Up(x,y,orientation,labyrinth)):
        neighbors.append(Node(x-1,y,orientation))
    if(Valid_Down(x,y,orientation,labyrinth)):
        neighbors.append(Node(x+1,y,orientation))
    if(Valid_Rotation(x,y,orientation,labyrinth)):
        if(orientation == "vertical"):
            neighbors.append(Node(x,y,"horizontal"))
        else:
            neighbors.append(Node(x,y,"vertical"))

    return neighbors