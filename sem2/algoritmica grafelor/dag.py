class DirectedAcyclicGraph:
    def __init__(self,n):

        self._g = []
        self._gt = []

    def addEdge(self, x, y):
        g[x].push_back(y)
        gt[y].push_back(x)

    def getNumberOfPaths(self, x, y):
        used=[]
        dp=[]
        dfs(x, dp, used)
        return dp[y]


def readGraph():
    #reading a directed graph from a text file.

    command = ''
    file_name = ''
    file_name = input("> Enter file name: ")
  #  while file_name not in ['test0.txt', 'bfs.txt','test.txt', 'test1.txt', 'graph100k.txt', 'graph10k.txt', 'graph1m.txt', 'graph1k.txt']:
   #     print("> Inexistent file.")
    #    file_name = input("> Enter file name: ") 

  #  f = open("%s" % file_name, "r")
    f = open("%s" % 'test0.txt', "r")

    print("> Loading...")

    ok = 1
    i = 0
    for line in f:
        if ok:
            n, m = line.split(' ')
            n = int(n)
            m = int(m)
            ok = 0
            G = DirectedAcyclicGraph()
        else:
           #-----------------------------------#
           # i += 1                             #
            #print ("> " + str((i*100)//m) + "%") #
            #sys.stdout.write("\033[F")         #
            #time.sleep(0)                      #
           #-----------------------------------#
            x, y = line.split(' ')
            m3 = G.addEdge(x, y)

    return G