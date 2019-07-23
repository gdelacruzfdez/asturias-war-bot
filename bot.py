import sys
import csv
from concejo import Concejo
from territory import Territory
from mapDrawer import MapDrawer
import numpy as np
import random

concejosFile = 'concejos.csv'

concejos = []

def readConcejosAndTerritories():
    concejos = []
    territories = []
    with open(concejosFile, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for i, row in enumerate(reader):
            concejos.append(Concejo(i, row[0]))
            territories.append(Territory(i, row[0], int(row[1]), int(row[2]), eval(row[3])))
    return concejos, territories

def generateCollisionMatrix(territories):
    size = len(territories)
    matrix = np.full((size, size), False)
    for territory in territories:
        for neighbour in territory.neighbours:
            matrix[territory.index][neighbour - 1] = True
    return matrix



drawer = MapDrawer('mapa.png', 'flag.png')

concejos, territories = readConcejosAndTerritories()
collisionMatrix = generateCollisionMatrix(territories)


while True:
    # Filter alive concejos
    aliveConcejos = filter(lambda c : c.isAlive(), concejos)
    # Select concejo that is going to atack
    attackerConcejo = random.choice(aliveConcejos)
    # Select concejo from which to attack
    attackSource = random.choice(attackerConcejo.owned)
    # Get possible objectives list
    possibleObjectives = map(lambda (i,x): i, filter(lambda (i,x): x, enumerate(collisionMatrix[attackSource])))
    # Select objective
    objectiveIndex = random.choice(possibleObjectives)
    objective = territories[objectiveIndex]
    # Add objective to list of owned territories
    previousOwnerIndex = objective.owner
    previousOwner = concejos[previousOwnerIndex]
    previousOwner.owned.remove(objectiveIndex)

    objective.owner = attackerConcejo.index
    attackerConcejo.owned.append(objectiveIndex)

    drawer.drawMap(territories, concejos, objective)
    
    print(attackerConcejo.name + ' ha conquistado ' + objective.name + ' previamente controlado por ' + previousOwner.name + '.')

    if not previousOwner.isAlive():
        print('El concejo de ' + previousOwner.name + ' ha sido completamente derrotado.')
    
    remainingAliveConcejos = sum(1 for i in aliveConcejos if i.isAlive())
    print(str(remainingAliveConcejos) + ' concejos restantes.')

    

