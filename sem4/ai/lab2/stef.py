from random import randint,random
#import matplotlib.pyplot as plt
import numpy as np

class Individ:
    def __init__(self, xmin=0, xmax=0, ymin=0, ymax=0):
        self.values = self.individual(xmin, xmax, ymin, ymax)
        self.fitness1 = 0.0
        self.fitness1 = self.fitness()
        
    def individual(self, xmin, xmax,ymin,ymax):
        '''
        Create a member of the population
        xmin: the minimum possible value for x
        xmax: the maximum possible value for x
        ymin: the minimum possible value for y
        ymax: the maximum possible value for y
        '''
        return [random()*(xmax-xmin)+xmin,random()*(ymax-ymin)+ymin]


    def getX(self):
        return self.values[0]
    
    def getY(self):
        return self.values[1]
        
    def fitness(self):
        """
        Determine the fitness of an individual. Lower is better.(min problem)
        For this problem we have the Cross-in-tray function
        
        individual: the individual to evaluate
        """
        x = self.getX()
        y = self.getY()
        f = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 *np. pi * x) + np.cos(2 * np.pi * y))) + np.e + 20
        return f
    def getFitness(self):
        return self.fitness1
        
    def mutate(self, pM, xmin, xmax, ymin, ymax): 
        '''
        Performs a mutation on an individual with the probability of pM.
        If the event will take place, at a random position a new value will be
        generated in the interval [vmin, vmax]
    
        individual:the individual to be mutated
        pM: the probability the mutation to occure
        vmin: the minimum possible value 
        vmax: the maximum possible value
        '''
        if pM > random():
            p = randint(0, 1)
            if p == 1:
                self.values[1] = random()*(ymax-ymin)+ymin
            else:
                self.values[0] = random()*(xmax-xmin)+xmin
    
    def crossover(self,p2):
        '''
        crossover between 2 parents
        Complete arithmetic crossover
        p1[i] = a * p1[i] + (1-a) * p2[i]
        p2[i] = (1-a) * p1[i] + a * p2[i] 
        '''
        a = random()
        self.values[0] = a * self.values[0] + (1-a) * p2[0]
        p2[0] = (1-a) * self.values[0] + a * p2[0] 
        
        self.values[1] = a * self.values[1] + (1-a) * p2[1]
        p2[1] = (1-a) * self.values[1] + a * p2[1] 
 
        return self,p2
    
    def blendcorssover(self,p2):
        child = [0,0]        
        a = random()
        m = min(self.values[0],p2[0])
        M = max(self.values[0],p2[0])
        i = M - m 
        down = m - i * a
        up = M - i * a
        child[0] = random()*(up - down) + down
        
        a = random()
        m = min(self.values[1],p2[1])
        M = max(self.values[1],p2[1])
        i = M - m 
        down = m - i * a
        up = M - i * a
        child[1] = random()*(up - down) + down
        newchild = Individ()
        newchild.values = child
        return newchild
    
    def __getitem__(self, key):
        return self.values[key]
    def __setitem__(self,key,c):
        self.values[key] = c
    
    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def __str__(self):
        return "("+str(self.values[0])+","+str(self.values[1])+")" 

class Population:
    def __init__(self,n,xmin,xmax,ymin,ymax):
        self.n = n
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.individs = self.population(self.n, xmin, xmax, ymin, ymax)
    
    def setFirst(self):
        self.individs = self.individs[:100]
        
    def getLen(self):
        return len(self.individs)
    
    def put(self,c):
        self.individs.append(c)

    def bestIndividual(self):
        return max(self.individs)
        
    def population(self,count,xmin, xmax, ymin, ymax):
        """
        Create a number of individuals (i.e. a population).
    
        count: the number of individuals in the population
        xmin: the minimum possible value for x
        xmax: the maximum possible value for x
        ymin: the minimum possible value for y
        ymax: the maximum possible value for y
        """
        l = []
        for x in range(count):
            individ = Individ(xmin, xmax, ymin, ymax)
            l.append(individ)
        return l
                    
    def selectForRecombination(self,dimension):
        recombPop = Population(0,0,0,0,0)
        strongParents = []
        
        for i in range(dimension):
            participants = []
            for j in range(3):
                p = self.individs[randint(0,len(self.individs) - 1 )]
                participants.append((p,p.fitness()))
                
            participants = sorted(participants,key=lambda p: p[1])
            strongParents.append(participants[0][0])
            
        recombPop.individs = strongParents
        return recombPop
        
    def selectForSurvival(self,newGen):
        for c in newGen:
            self.individs.append(c)
           
        strongIndivids = [] 
        for i in range(self.n):
            participants = []
            for j in range(3):
                p = self.individs[randint(0,len(self.individs) - 1 )]
                participants.append((p,p.fitness()))
                
            participants = sorted(participants,key=lambda p: p[1])
            strongIndivids.append(participants[0][0])
            
        self.individs = strongIndivids

    
    def __getitem__(self, key):
        return self.individs[key]
    def __setitem__(self,key,c):
        self.individs[key] = c
    def __str__(self):
        s = ""
        for i in range(self.getLen()-97):
            s += " "+str(self.individs[i])+" ->"+str(self.individs[i].fitness())+" " 
        return s

class Problem:
    def __init__(self):
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0
        self.dimPopulation = 100
        self.pM=0.01
        
    def getXMin(self):
        return self.xmin
    def getXMax(self):
        return self.xmax
    def getYMin(self):
        return self.ymin
    def getYMax(self):
        return self.ymax
    def getDimPop(self):
        return self.dimPopulation
    def getPM(self):
        return self.pM   
    
    def loadData(self,fileName):
        attrs = []
        f = open(fileName, "r")
        line = f.readline().strip()
        while line != "":
            elem = line.split("=")
            attrs.append(elem[1])     
            line = f.readline().strip()       
        f.close()
        
        self.xmin = int(attrs[0])
        self.xmax = int(attrs[1])
        self.ymin = int(attrs[2])
        self.ymax = int(attrs[3])
        self.dimPopulation = int(attrs[4])
        self.pM = float(attrs[5])


class Algorithm():
    def __init__(self):
        self.problem = Problem()
        self.readProblem()
        self.pop = Population(self.problem.getDimPop(),self.problem.getXMin(), self.problem.getXMax(), self.problem.getYMin(), self.problem.getYMax())
        
            
        
    def readProblem(self):
        self.problem.loadData("D:\sem4\AI\lab2\input.txt")
    
    def run(self,noIteratii):  
        
        results = []
        for i in range(noIteratii):
            self.iteration(self.pop, self.problem.getPM(), self.problem.getXMin(), self.problem.getXMax(), self.problem.getYMin(), self.problem.getYMax())
            
            fitnessValues = []
            for x in self.pop.individs:
                fitnessValues.append(x.fitness())
            fitnessValues = sorted(fitnessValues)
                  
           
            results.append(fitnessValues[0])
    
        """ arr = np.array(results)
        m = np.mean(arr,axis=0)
        means=[]
        for i in range(noIteratii):
            means.append(m)
        plt.plot(range(0,noIteratii),means)
        plt.plot( range(0,noIteratii),results)
        plt.show()
        """
        return fitnessValues[0]
            

    
    def iteration(self,pop, pM, xmin, xmax, ymin, ymax):
        '''
        an iteration
    
        pop: the current population
        pM: the probability the mutation to occur
        xmin, xmax, ymin, ymax: bounds for x and y
        '''
        newGen = []
        
        recompPop = self.pop.selectForRecombination(self.problem.getDimPop() // 2)
        for i in range(self.problem.getDimPop() // 2):
            i1=randint(0,recompPop.getLen()-1)
            i2=randint(0,recompPop.getLen()-1)
            if (i1!=i2):
                c=recompPop[i1].blendcorssover(recompPop[i2])
                c.mutate(pM, xmin, xmax, ymin, ymax)
                #c2.mutate(pM,xmin,xmax,ymin,ymax)
                newGen.append(c)
            else:
                i-=1
        self.pop.selectForSurvival(newGen)

    def statistics(self, generations, tests):
        fitnesses = []
        for test in range(tests):
            self.pop = Population(30,-5,5,-5,5)
            self.run(100)
            print(self.pop.bestIndividual())

            fitnesses.append(self.pop.bestIndividual().getFitness())

        arr = np.array(fitnesses)

        mean = np.mean(arr, axis=0)
        std = np.std(arr, axis=0)

        print("Mean: %.4f" % mean)
        print("Std:  %.4f" % std)

def main():
    a = Algorithm()

   # a.statistics(100,30)
    return a.run(100)

if __name__ == '__main__':
    results = []
    for i in range(30):
        results.append(main())

    
    print(results)
    arr = np.array(results)
    m = np.mean(arr,axis=0)
    means=[]
    for i in range(30):
        means.append(m)
    print(m)
    print(means)
    print("r")
    print(results)
