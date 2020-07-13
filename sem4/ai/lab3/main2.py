#!/bin/python3
from collections import deque
from math import sin, cos, sqrt, exp, pi
from random import random, uniform
import numpy 

import matplotlib.pyplot as plt
import logging

class Problem:
    functions = {
        'Ackley':{
            'xMin': -5,
            'xMax': 5,
            'xLabel': -4,
            'yMin': -5,
            'yMax': 5,
            'yLabel': 3.2,
            'population': 1000,
            'maxIterations': 1000,
            'omega': 0.005,
            'phiP': 0.025,
            'phiG': 0.025,
            'particleSize': 4,
            'f': lambda p: -20 * numpy.exp(-0.2 * sqrt(0.5 * (p[0] * p[0] + p[1] * p[1]))) + 20 - numpy.exp(0.5 * (numpy.cos(2 * pi * p[0]) + numpy.cos(2 * pi * p[1]))) + numpy.e

        },
        'Cross-in-tray': {
            'xMin': -10,
            'xMax': 10,
            'xLabel': -9.7,
            'yMin': -10,
            'yMax': 10,
            'yLabel': 7.7,
            'population': 100,
            'maxIterations': 1000,
            'omega': 0.005,
            'phiP': 0.025,
            'phiG': 0.025,
            'particleSize': 3,
            'f': lambda p: -0.0001 * (abs(sin(p[0]) * sin(p[1]) * exp(100 - sqrt(p[0]**2 + p[1]**2) / pi)) + 1) ** 0.1
        }
    }

    function = 'Ackley'
    config = functions[function]

    xBound = abs(config['xMax'] - config['xMin'])
    yBound = abs(config['yMax'] - config['yMin'])

    iterationsShown = 10
    clearBetweenIterations = False
    saveFrames = False

    def fitness(position):
        return Problem.config['f'](position)


class Particle:

    def __init__(self, swarm=None):
        self.setRandomPosition()
        self.setRandomVelocity()

        self.bestPosition = self.position
        self.swarm = swarm

    def __repr__(self):
        return "Particle(%.2f, %.2f)" % self.position

    def setRandomPosition(self):
        x = uniform(Problem.config['xMin'], Problem.config['xMax'])
        y = uniform(Problem.config['yMin'], Problem.config['yMax'])

        self.position = (x, y)

    def setRandomVelocity(self):
        dx = uniform(-Problem.xBound, Problem.xBound)
        dy = uniform(-Problem.yBound, Problem.yBound)

        self.velocity = (dx, dy)

    def updateVelocity(self, i, p, g):
        newComponent = Problem.config['omega'] * self.velocity[i] \
            + Problem.config['phiP'] * p * (self.bestPosition[i] - self.position[i]) \
            + Problem.config['phiG'] * g * \
            (self.swarm.bestPosition[i] - self.position[i])

        if i == 0:
            self.velocity = (newComponent, self.velocity[1])
        else:
            self.velocity = (self.velocity[0], newComponent)

    def updatePosition(self):
        newX = max(min(self.position[0] + self.velocity[0],
                       Problem.config['xMax']), Problem.config['xMin'])
        newY = max(min(self.position[1] + self.velocity[1],
                       Problem.config['yMax']), Problem.config['yMin'])

        self.position = (newX, newY)

    def updateBestPosition(self):
        self.bestPosition = self.position


class SwarmPlot:

    def __init__(self, swarm):
        self.swarm = swarm
        self.currentlyPlotted = {
            'iterations': deque([]),
            'text': None
        }

    def clearOldPoints(self):
        iterations = self.currentlyPlotted['iterations']
        if len(iterations) > Problem.iterationsShown:
            iterations[0].remove()
            iterations.popleft()

    def plotCurrentIteration(self):
        plt.axis([Problem.config['xMin'], Problem.config['xMax'],
                  Problem.config['yMin'], Problem.config['yMax']])

        particles = self.swarm.particles
        xs = list(map(lambda particle: particle.position[0], particles))
        ys = list(map(lambda particle: particle.position[1], particles))

        newIteration = plt.scatter(xs, ys, s=Problem.config['particleSize'])
        self.currentlyPlotted['iterations'].append(newIteration)

    def plotText(self, iteration):
        bestPosition = self.swarm.bestPosition
        bestFitness = Problem.config['f'](bestPosition)

        figureText = 'Iteration %i\n' % iteration + \
                     'Best particle: (%.5f, %.5f)\n' % bestPosition + \
                     'Best fitness:  %.6f' % bestFitness

        self.currentlyPlotted['text'] = plt.text(
            Problem.config['xLabel'],
            Problem.config['yLabel'],
            figureText,
            bbox=dict(facecolor='blue', alpha=0.4),
            fontsize=10,
            family="Ubuntu Mono")

    def clearOldText(self):
        if self.currentlyPlotted['text'] is not None:
            self.currentlyPlotted['text'].remove()

    def plotEverything(self, iteration):
        if Problem.clearBetweenIterations:
            plt.clf()

        self.plotCurrentIteration()
        self.clearOldPoints()
        self.clearOldText()
        self.plotText(iteration)

        if iteration == 1:
            plt.tight_layout()

        if Problem.saveFrames:
            plt.savefig("img/%s-%i.png" % (Problem.function, iteration), dpi=200,
                        orientation='landscape')

        plt.pause(0.0001)


class Swarm:

    def __init__(self, population):
        self.particles = [Particle(swarm=self) for _ in range(population)]
        self.bestPosition = min([x.position for x in self.particles],
                                key=lambda x: Problem.fitness(x))
        self.plot = SwarmPlot(self)

    def simulate(self):
        for iteration in range(1, 1 + Problem.config['maxIterations']):
            logging.info("ITERATION #%i" % iteration)

            self.plot.plotEverything(iteration)

            for particle in self.particles:
                for dimension in range(2):
                    p, g = random(), random()
                    particle.updateVelocity(dimension, p, g)
                particle.updatePosition()

                if Problem.fitness(particle.position) < Problem.fitness(particle.bestPosition):
                    particle.updateBestPosition()

                    if Problem.fitness(particle.bestPosition) < Problem.fitness(self.bestPosition):
                        self.bestPosition = particle.bestPosition

            logging.info("CURRENT SOLUTION: (%.3f, %.3f)" % self.bestPosition)


def main():
    logging.basicConfig(level=logging.INFO)

    swarm = Swarm(Problem.config['population'])
    swarm.simulate()

    logging.info("Found best position = (%.6f, %.6f) " % swarm.bestPosition +
                 "after %i iterations" % Problem.config['maxIterations'])

if __name__ == '__main__':
    main()