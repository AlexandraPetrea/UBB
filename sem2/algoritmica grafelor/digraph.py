import os
from queue import PriorityQueue
from collections import defaultdict, deque

class MyException(Exception):
    pass

class Cost:
    def __init__(self):
        self._vertices = {}

    def addCost(self, x, y, c):

        ''' Adds a cost to the dict of cost '''

        if x not in self._vertices.keys():
            return "> Vertex " + str(x) + "does not exist."

        if y not in self._vertices.keys():
            return "> Vertex " + str(y) + "does not exist."

        self._vertices[x].append((y, c))

    def removeCost(self, x, y):

        ''' Removes a cost from an edge '''

        if x not in self._vertices.keys():
            return "> Vertex does not exist."

        for t in self._vertices[x]:
            if t[0] == y:
                self._vertices[x].remove(t)

     #   if x in self._outEdges:
      #      self._outEdges.pop(x)

    def getCost(self, x, y):

        ''' Returning the cost of the edge from x to y ''' 

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return "> Invalid input."

        if x not in self._vertices.keys():
            return "> Vertex " + str(x) + " does not exist."

        if y not in self._vertices.keys():
            return "> Vertex " + str(y) + " does not exist."

        for t in self._vertices[x]:
            if t[0] == y:
                return "> The cost from " + str(x) + " to " + str(y) + " is " + str(t[1]) + "."

    def setCost(self, x, y, c):

        ''' Updating the cost of the edge from x to y '''

        try:
            x = int(x)
            y = int(y)
            c = int(c)
        except ValueError:
            return "> Invalid input."

        if x not in self._vertices.keys():
            return "> Vertex " + str(x) + " does not exist."

        if y not in self._vertices.keys():
            return "> Vertex " + str(y) + " does not exist."

        for t in self._vertices[x]:
            if t[0] == y:
                self._vertices[x].remove(t)
                self._vertices[x].append((y, c))
                return "> Update successful."

class DiGraph:
    def __init__(self,n, undirected):
        '''
        vertices: the key is a vertex v, the value is a list of tuples
                        (u, c) with the meaning that there is an edge from
                        v to u of cost c
        outEdges: the key is a vertex v, the value is a list of vertices
                        u, with the meaning that there is an edge from v to u
        inEdges: the key is a vertex v, the value is a list of vertices
                        u, with the meaning that there is an edge from u to v
        '''

        self._outEdges = {}
        self._inEdges = {}
        self._vertices = {}
        self._undirected = []

        for i in range(n):
            self._outEdges[i]=[]
            self._inEdges[i]=[]

    def parseX(self):

        '''Returns an iterable containing all the vertices'''

        return self._vertices.keys()

    def parseNin(self,x):

        '''Returns an iterable containing the inbound neighbours of x'''

        return self._inEdges[x]

    def parseNout(self, x):
        
        '''Returns an iterable containing the outbound neighbours of x'''

        return self._outEdges[x]

    def isVertex(self, v):

        ''' Checks if v is a vertex or not '''

        if v not in self.parseX():
           raise MyException("\n > Vertex " + str(v) + " doesn't exist. \n")

    def getVertices(self):

        '''Returns the number of vertices in the graph''' 

        return len(self._vertices)

    def addVertex(self, v):

        ''' Adds a vertex to the graph '''

        try:
            v = int(v)
        except ValueError:
            return "> Invalid input."

        if v in self._vertices.keys():
           return "> Vertex already exists."

        self._vertices[v] = []
        self._outEdges[v]=[]
        self._inEdges[v]=[]

        return "> Vertex was successfully added."

    def removeVertex(self, v):

        ''' Removes a vertex from the graph along with all the edges that come into contact with that vertex '''

        try:
            v = int(v)
        except ValueError:
            return "> Invalid input."

        if v not in self._inEdges:
           return "> Vertex doesn't exist."

        if v not in self._outEdges:
           return "> Vertex doesn't exist."

        if v in self._outEdges:
            for node in self._outEdges[v]:
                self._inEdges[node].remove(v)

        if v in self._inEdges:
            for node in self._inEdges[v]:
                self._outEdges[node].remove(v)
            for node in self._inEdges[v]:
               # for t in self._vertices[node]:
                  #  if t[0] == v:
                        #self._vertices[node].remove(t)
                Cost.removeCost(self, node, v)


        if v in self._inEdges:
            self._inEdges.pop(v)
        if v in self._outEdges:
            self._outEdges.pop(v)
        if v in self._vertices:
            self._vertices.pop(v)
        return "> Vertex was successfully removed."

    def isEdge(self, x, y):

        '''Check to see if there is an edge between x and y
         x -----> y'''

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return 2

        if x in self._outEdges:
            if y in self._outEdges[x]:
                return 1

        return 0

    def addEdge(self, x, y, c):

        ''' Adds an edge from x to y with the cost c to the graph '''

        try:
            x = int(x)
            y = int(y)
            c = int(c)
        except ValueError:
            return "> Invalid input."

        if x not in self._inEdges:
            return "> Invalid vertex."

        if y not in self._outEdges:
            return "> Invalid vertex."


        if self.isEdge(x, y):
            return "> Edge already exists, cannot overwrite."

        #self._vertices[x].append((y, c))
        self._undirected.append([x,y,c])
        Cost.addCost(self, x, y, c)

        if y in self._inEdges.keys():
            self._inEdges[y].append(x)
        else:
            self._inEdges[y] = [x]

        if x in self._outEdges.keys():
            self._outEdges[x].append(y)
        else:
            self._outEdges[x] = [y]

        if self._undirected:
            Cost.addCost(self, x, y, c)
            if x in self._inEdges.keys():
                self._inEdges[x].append(y)
            else:
                self._inEdges[x] = [y]

            if y in self._outEdges.keys():
                self._outEdges[y].append(x)
            else:
                self._outEdges[y] = [x]


        return "> Edge was successfully added."

    def removeEdge(self, x, y):
        
        ''' Removes an edge from the graph ''' 

        x = int(x)
        y = int(y)

        # Remove y from the OutEdges of x

        self._outEdges[x].remove(y)

        # Remove x from the InEdges of y

        self._inEdges[y].remove(x)

        # Remove y from self.vertices[x]

        Cost.removeCost(self, x, y)
        return "> Edge was successfully removed."

    def inDegree(self, v):

        ''' Returning the inDegree of a vertex '''

        x = 0
        v = int(v)

        for obj in self._inEdges:
            if obj == v:
                x = len(self._inEdges[obj])
                break

        return v, x

    def outDegree(self, v):

        ''' Returning the outDegree of a vertex '''

        x = 0
        v = int(v)

        for obj in self._outEdges:
            if obj == v:
                x = len(self._outEdges[obj])
                break

        return v, x

    def inBound(self, v):

        ''' Return the inBound edges (vertex, cost) '''

        v = int(v)

        if v not in self._inEdges or len(self._inEdges[v]) == 0:
            return "> No inbound edges."

        message = "> Inbound edges:\n"

        for t in self._inEdges[v]:
            message += "  " + str(t)

        return message

    def outBound(self, v):

        ''' Return the outBound edges (vertex, cost) ''' 

        v = int(v)

        if v not in self._outEdges or len(self._outEdges[v]) == 0:
            return "> No outbound edges."

        message = "> Outbound edges:\n"

        for t in self._outEdges[v]:
            message += "  " + str(t)

        return message

    def printG(self):

        ''' Print the graph like x <-- y '''

        for x in self.parseX():
            print ("%s:" % x)
            for y in self.parseNin(x):
                print ("%s <- %s" % (x, y))

    def printCost(self):

        '''Print the graph with the cost '''

        for i in range(self.getVertices()):
            if(self.outDegree(i)[1] != 0):
                print ("%s:" % i)
                for y in self.parseNout(i):
                    print (Cost.getCost(self, i,y))

    def bfs(self, start, end):

        '''Return the lowest length path between start and end, by using a backward breadth-first search from the end vertex '''
        queue = [[end]]
        visited = set()

        while queue:
            # Gets the first path in the queue
            path = queue.pop(0)

            # Gets the last node in the path
            vertex = path[-1]

            # Checks if we got to the end
            if vertex == start:
                return path
            # We check if the current node is already in the visited nodes set in order not to recheck it
            elif vertex not in visited:
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                for current_neighbour in self._inEdges[vertex]:
                    new_path = list(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)

                # Mark the vertex as visited
                visited.add(vertex)

    def DFSUtil(self,v,visited,S):

        # Mark the current node as visited and make a list with the nodes
        visited[v]= True
        S.append(v)
        #Recur for all the vertices adjacent to this vertex
        for j in self._outEdges[v]:
            if visited[j]==False:
                self.DFSUtil(j,visited,S)
        return S

        
    def fillOrder(self,v,visited, stack):

        # Mark the current node as visited 
        visited[v]= True

        #Recur for all the vertices adjacent to this vertex
        for i in self._outEdges[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = DiGraph(self.getVertices(), False)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self._vertices:
            for j in self._outEdges[i]:
                g.addEdge(j,i,0)
        return g

  
    # The main function that finds and prints all strongly connected components
    def printSCCs(self):
         
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.getVertices())
        # Fill vertices in stack according to their finishing times
        for i in range(self.getVertices()):
            if visited[i]==False:
                self.fillOrder(i, visited, stack)
 
        # Create a reversed graph
        gr = self.getTranspose()
         
        # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.getVertices())
 
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            S =[]
            if visited[i]==False:
                aux = gr.DFSUtil(i, visited,S)
                print(aux)
                print("")

    def floydwarshall(graph):
 
    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
        dist = {}
        pred = {}
        for u in range(0,graph.getVertices()):
            dist[u] = {}
            pred[u] = {}
            for v in range(0,graph.getVertices()):
                dist[u][v] = 10000
                pred[u][v] = -1
            dist[u][u] = 0
            for neighbor in graph._vertices[u]:
                dist[u][neighbor[0]] = neighbor[1]
                pred[u][neighbor[0]] = u
                #print(neighbor[0], dist[u][neighbor[0]], pred[u][neighbor[0]])
 
        for t in range(0,graph.getVertices()):
            # given dist u to v, check if path u - t - v is shorter
            for u in range(0,graph.getVertices()):
                for v in range(0,graph.getVertices()):
                    if dist[u][t] + dist[t][v] < dist[u][v]:
                        dist[u][v] = dist[u][t] + dist[t][v]
                        pred[u][v] = pred[t][v] # route new path through t

 
        return dist, pred   

    def constructPath(self, pred, i, j, path):
        i,j = int(i), int(j)
        if(i==j):
            path.append(i)
        else:
            if (pred[i][j] != -1):
                self.constructPath(pred, i, pred[i][j], path);
                path.append(j)

    #KRUSKAL
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
 
        result =[] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
            # Sort all the edges in non-decreasing order of their weight
        self._undirected =  sorted(self._undirected,key=lambda item: item[2])
 
        parent = [] ; rank = []
 
        # Create v subsets with single elements
        for node in range(self.getVertices()):
            parent.append(node)
            rank.append(0)
     
        # Number of edges to be taken is equal to v-1
        while e < self.getVertices() -1 :
 
            # Pick the smallest edge and increment the index for next iteration
            u,v,w =  self._undirected[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge doesn't cause cycle, include it in result and increment the index of result for next edge
            if x != y:
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, x, y)            
            # Else discard the edge

        return result

    ################## HAMILTONIAN ###############

    def isSafe(self, v, pos, path):
        # Check if current vertex and last vertex 
        # in path are adjacent
        if not self.isEdge(path[pos-1], v):
            return False
 
        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False
 
        return True
 
    # A recursive utility function to solve 
    # hamiltonian cycle problem
    def hamCycleUtil(self, path, pos):
 
        # base case: if all vertices are 
        # included in the path
        if pos == self.getVertices():
            # Last vertex must be adjacent to the 
            # first vertex in path to make a cyle
            if self.isEdge(path[pos-1], path[0]) :
                return True
            else:
                return False
 
        # Try different vertices as a next candidate 
        # in Hamiltonian Cycle. We don't try for 0 as 
        # we included 0 as starting point in in hamCycle()
        for v in range(1,self.getVertices()):
 
            if self.isSafe(v, pos, path) == True:
 
                path[pos] = v
 
                if self.hamCycleUtil(path, pos+1) == True:
                    return True
 
                # Remove current vertex if it doesn't 
                # lead to a solution
                path[pos] = -1
 
        return False
 
    def hamCycle(self):
        path = [-1] * self.getVertices()
 
        ''' Let us put vertex 0 as the first vertex 
            in the path. If there is a Hamiltonian Cycle, 
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0
 
        if self.hamCycleUtil(path,1) == False:
           # print ("Solution does not exist\n")
            return False, path
        else :
       # self.printSolution(path)
            return True, path

    def floydwarshall2(graph):
 
    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
        dist = {}
        pred = {}
        for u in range(0,graph.getVertices()):
            dist[u] = {}
            pred[u] = {}
            for v in range(0,graph.getVertices()):
                dist[u][v] = 10000
                pred[u][v] = -1
            dist[u][u] = 10000
            for neighbor in graph._vertices[u]:
                dist[u][neighbor[0]] = neighbor[1]
                pred[u][neighbor[0]] = u
 
        for t in range(0,graph.getVertices()):
            # given dist u to v, check if path u - t - v is shorter
            for u in range(0,graph.getVertices()):
                for v in range(0,graph.getVertices()):
                    if dist[u][t] + dist[t][v] < dist[u][v]:
                        dist[u][v] = dist[u][t] + dist[t][v]
                        pred[u][v] = pred[t][v] # route new path through t

 
        return dist, pred
 

