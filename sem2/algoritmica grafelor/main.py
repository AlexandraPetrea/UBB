import os
import os.path
import sys
import time
from digraph import *

def readGraph():
    #reading a directed graph from a text file.

    command = ''
    file_name = ''
    file_name = input("> Enter file name: ")
    while file_name not in ['test0.txt', 'graph2k.txt', 'bfs.txt','test.txt', 'test1.txt', 'graph100k.txt', 'graph10k.txt', 'graph1m.txt', 'graph1k.txt']:
        print("> Inexistent file.")
        file_name = input("> Enter file name: ") 

    f = open("%s" % file_name, "r")
    #f = open("%s" % 'test0.txt', "r")

    print("> Loading...")

    ok = 1
    i = 0
    for line in f:
        if ok:
            n, m = line.split(' ')
            n = int(n)
            m = int(m)
            ok = 0
            G = DiGraph(n, False)
        else:
           #-----------------------------------#
           # i += 1                             #
            #print ("> " + str((i*100)//m) + "%") #
            #sys.stdout.write("\033[F")         #
            #time.sleep(0)                      #
           #-----------------------------------#
            x, y, c = line.split(' ')
            if y == -1 and c == -1:
                G.addVertex(x)
            else:
                m1 = G.addVertex(x)
                m2 = G.addVertex(y)
                m3 = G.addEdge(x, y, c)

    # In case there are isolated vertices, we add them to the graph
    for i in range(n):
        if i not in G._vertices:
            G.addVertex(i)

    print("> 100%")
    print("> Graph successfully loaded.")
    return G

def showMenu():
    print("> Select a command: ")
    print("  1 - Add a vertex")
    print("  2 - Remove a vertex")
    print("  3 - Add an edge")
    print("  4 - Remove an edge")
    print("  5 - Get number of vertices")
    print("  6 - Check if an edge exists")
    print("  7 - Degrees of a vertex")
    print("  8 - Show inBound edges of a vertex")
    print("  9 - Show outBound edges of a vertex")
    print(" 10 - Get the cost of an edge")
    print(" 11 - Set the cost of an edge")
    print(" 12 - Print the cost for all the graph ")
    print(" 13 - Print the graph")
    print(" 14 - Return the lowest length path between 2 vertices")
    print(" 15 - Return the strongly connected components")
    print(" 16 - Return the shortest path between 2 vertices using Floyd-Warshall")
    print(" 17 - Return the minimum spanning tree using Kruskal")
    print(" 18 - Return the Hamiltonian cycle(if exists)")
    print("  h - Help")
    print("  0 - Exit")

def printGraph(G):
    ''' Print the graph '''
    aux = G.getVertices()
    i = 0
    n = 0
    while(n < aux):
        if i in G._vertices.keys():
            print (i, G.parseNin(i), G.parseNout(i))
            n = n + 1
        i = i + 1

def main():

    G = readGraph()
   # printGraph(G)
   # print("aici", G.getVertices())
    showMenu()

    while (1):

        command = input("> ")

        if command == 'h':
            showMenu()
            continue

        try:
            command = int(command)
        except ValueError:
            print("> Invalid command.")
            continue

        if command == 1:

            # Add a vertex

            v = input("> Vertex: ")
            message = G.addVertex(v)

            print(message)

        elif command == 2:

            # Remove a vertex

            v = input("> Vertex to be removed: ")
            message = G.removeVertex(v)

            print(message)

        elif command == 3:

            # Add an edge

            x = input("> Source vertex: ")
            y = input("> Target vertex: ")
            c = input("> Edge cost: ")

            message = G.addEdge(x, y, c)

            print(message)

        elif command == 4:

            # Remove an edge

            x = input("> Source vertex: ")
            y = input("> Target vertex: ")

            errorMessage = G.isEdge(x, y)

            if errorMessage == 2:
                print("> Invalid input.")
                continue
            elif errorMessage == 0:
                print("> Inexistent edge.")
                continue
            else:
                message = G.removeEdge(x, y)

            print (message)

        elif command == 5:

            # Get the number of vertices

            numOfVertices = G.getVertices()
            if numOfVertices == 0:
                print("> There are NO vertices in the graph.")
            elif numOfVertices == 1:
                print("> There is only one vertex in the graph.")
            else:
                print("> There are " + str(G.getVertices()) + " vertices in the graph.")

        elif command == 6:

            # Check in an edge exists

            x = input("> Source vertex: ")
            y = input("> Target vertex: ")

            errorMessage = G.isEdge(x, y)

            if errorMessage == 2:
                print("> Invalid input.")
            elif errorMessage == 0:
                print("> Inexistent edge.")
            else:
                print("> Edge exists.")

        elif command == 7:

            # Degrees of a vertex

            v = input("> Vertex: ")

            try:
                v = int(v)
            except ValueError:
                print ("> Invalid input.")
                continue

            if v not in G._vertices.keys():
                print ("> Vertex does not exist.")
            else:
                a, b = G.inDegree(v)
                c, d = G.outDegree(v)
                print ("> inDegree of " + str(a) + " is " + str(b) + ".")
                print ("> outDegree of " + str(c) + " is " + str(d) + ".")

        elif command == 8:

            # Show inBound edges of a vertex

            v = input("> Vertex: ")

            try:
                v = int(v)
            except ValueError:
                print ("> Invalid input.")
                continue

            message = G.inBound(v)

            print (message)

        elif command == 9:

            # Show outBound edges of a vertex

            v = input("> Vertex: ")

            try:
                v = int(v)
            except ValueError:
                print ("> Invalid input.")
                continue

            message = G.outBound(v)

            print (message)

        elif command == 10:

            # Get the cost of an edge

            x = input("> Source vertex: ")
            y = input("> Target vertex: ")

            errorMessage = G.isEdge(x, y)

            if errorMessage == 2:
                print("> Invalid input.")
            elif errorMessage == 0:
                print("> Inexistent edge.")
            else:
                print (Cost.getCost(G, x, y))

        elif command == 11:

            # Set the cost of an edge

            x = input("> Source vertex: ")
            y = input("> Target vertex: ")
            c = input("> The new cost: ")

            errorMessage = G.isEdge(x, y)

            if errorMessage == 2:
                print("> Invalid input.")
            elif errorMessage == 0:
                print("> Inexistent edge.")
            else:
                print (Cost.setCost(G, x, y, c))
                #print("> Update successful.")

        elif command == 12:

            # Print the cost of whole graph

            G.printCost()

        elif command == 13:

            #Print the whole grap

            printGraph(G)

        elif command == 14:

            #BFS backward 
            
            start = input("> Start vertex: ")

            try:
                start = int(start)
                G.isVertex(start)
            except ValueError:
                print ("> Invalid input.")
                continue
            except MyException as msg:
                print(msg)
                continue


            end = input("> End vertex: ")

            try:
                end = int(end)
                G.isVertex(end)
            except ValueError:
                print ("> Invalid input.")
                continue
            except MyException as msg:
                print(msg)
                continue

            aux = G.bfs(start, end)
            print("the length is", len(aux)-1)


            if(aux == None):
                print("There is no path between them")
            else:
                print(aux)

        elif command == 15:

            #Print the strongly connected components
            
            G.printSCCs();

        elif command == 0:
            print("> Exiting...")
            exit(0)

        elif command == 16:

            #Print the shortest path

            start = input("> Start vertex: ")

            try:
                start = int(start)
                G.isVertex(start)
            except ValueError:
                print ("> Invalid input.")
                continue
            except MyException as msg:
                print(msg)
                continue

            end = input("> End vertex: ")

            try:
                end = int(end)
                G.isVertex(end)
            except ValueError:
                print ("> Invalid input.")
                continue
            except MyException as msg:
                print(msg)
                continue

            dist, pred = G.floydwarshall();
            #print ("Predecesors in shortest path")
            #for v in pred: 
             #   print (v, pred[v])

            #print ("Shortest distance from each vertex")
            #for v in dist: print (v, dist[v])

            cost = dist[start][end]
            path=[]
            G.constructPath(pred, start, end, path)
            if(path == []):
               print("Inexistent path")
            else:
                print("The path is:", path)
                print("cost is: ", cost)

        elif command == 17:
            aux = G.KruskalMST();

            print ("Following are the edges in the constructed MST")
            for u,v,weight  in aux:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
                print ("%d - %d = %d" % (u,v,weight))
           

        elif command == 18:
            ok, path = G.hamCycle();
            if (ok == False):
                print("There is no Hamiltonian cycle")
            else:
                print ("The Hamiltonian cycle")
                for vertex in path:
                    print (vertex)
                print (path[0])

        elif command == 19:
            dist, pred = G.floydwarshall2();
            print(dist[0][0])
            print(dist[1][1])            
            print(dist[2][2])
            print(dist[3][3])



main()