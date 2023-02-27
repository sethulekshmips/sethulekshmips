from queue import PriorityQueue
def ucs(graph,start,goal):
    pq = PriorityQueue()
    pq.put((0,start))
    explored = set()

    while not pq.empty():
        cost,currnode=pq.get()
        if currnode==goal:
            return cost
        else:
            explored.add(currnode)
            for neighbour,neighbour_cost in graph[currnode].items():
                if neighbour is not explored:
                    totalcost = cost+neighbour_cost
                    pq.put((totalcost,neighbour))
                else:
                    return None
graph = {'A':{'B':5,'C':1},
       'B':{'D':3 },
         'C':{'D':2},
         'D':{'E':4},
         'E':{}}
path_cost = ucs(graph,'A','E')
print(path_cost)