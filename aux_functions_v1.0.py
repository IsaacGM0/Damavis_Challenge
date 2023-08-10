def Valid_Labyrinth_Range(labyrinth): #Valid that the matrix has the dimensions (X,Y) where 3<=X,Y<=1000.

    if (3 > len(labyrinth) | len(labyrinth)>1000):
        return False
    len_labyrinth=len(labyrinth[0]) #Check if the matrix is ​​rectangular.
    for i in labyrinth:
        if(3 > len(i) and len(i)>1000 and len_labyrinth == len(i)):
            return False
    return True

def Valid_Labyrinth_Symbols(labyrinth): #Checks if the matrix only has "." and "#".
    for i in labyrinth:
        for j in i:
            if not  (j == "#" or  j == "." ):
                return False     
    return True

