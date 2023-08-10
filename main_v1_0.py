from aux_functions_v1_3 import *
from examples import *


def main(labyrinth):
    start=Node(0,1,"horizontal")
    goal=Node(9,8,"horizontal")
    if not (Valid_Labyrinth_Range(labyrinth)):
        return print("Matrix no rectangular")
    
    if not (Valid_Labyrinth_Symbols(labyrinth)):
        return print("The matrix contains elements other than . and # ")
        
    
    open_list = [start]
    closed_set = set()
    a=0
    while open_list and a<1500: #Apply A* algorithm
        a=a+1
        current = open_list.pop(0)
        closed_set.add((current.x, current.y,current.orientation))

        if current.x == goal.x and current.y == goal.y:
            path = []
            counter=-1
            while current:
                path.insert(0, (current.x, current.y))
                current = current.parent
            if path:
                print("Camino encontrado:")
                for x, y in path:
                    print(f"({x}, {y})")
                    counter+=1
            else:
                print("No se encontró un camino.")
            print(counter)
            return counter

        neighbors = Find_Neighbors(current.x,current.y,current.orientation,labyrinth)
        for one_neighbor in neighbors:
                one_neighbor.parent = current
                if (one_neighbor.x, one_neighbor.y,one_neighbor.orientation) not in closed_set:
                    open_list.append(one_neighbor)
                    closed_set.add((one_neighbor.x, one_neighbor.y,one_neighbor.orientation))
        


    return -1

print(main(labyrinth4))