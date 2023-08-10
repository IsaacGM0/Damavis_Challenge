from aux_functions_v2_0 import *
from examples import *


def main(labyrinth):
    if not (Valid_Labyrinth_Range(labyrinth)):
        return print("Matrix no rectangular")
    
    if not (Valid_Labyrinth_Symbols(labyrinth)):
        return print("The matrix contains elements other than . and # ")
        
    start_node=Valid_Start_Node(labyrinth)
    goal1=Node(len(labyrinth)-1,len(labyrinth[0])-2,"horizontal")
    goal2=Node(len(labyrinth)-2,len(labyrinth[0])-1,"vertical")
    solutions=[]
    if (start_node == []):
        return print("This labyrinth has obstacles at the start")
    for start in start_node:       #Apply A* algorithm. First with rod starting in (0,1) and next (1,0)
        open_list = [start]
        closed_set = set()
        solution=0
        a=0
        while open_list and solution==0: 
            a=a+1
            current = open_list.pop(0)
            closed_set.add((current.x, current.y,current.orientation))

            if (current.x == goal1.x and current.y == goal1.y) or (current.x == goal2.x and current.y == goal2.y):
                path = []
                solution=-1
                while current:
                    path.insert(0, (current.x, current.y))
                    current = current.parent
                if path:
                    #print("Camino encontrado:")
                    for x, y in path:
                        #print(f"({x}, {y})")  this comment is if you want to know the path
                        solution+=1


            if(solution==0):
                neighbors = Find_Neighbors(current.x,current.y,current.orientation,labyrinth)
                for one_neighbor in neighbors:
                        one_neighbor.parent = current
                        if (one_neighbor.x, one_neighbor.y,one_neighbor.orientation) not in closed_set:
                            open_list.append(one_neighbor)
                            closed_set.add((one_neighbor.x, one_neighbor.y,one_neighbor.orientation))
        solutions.append(solution)
    if (min(solutions)==0):
        return -1
    else:
        return min(solutions)
        


    