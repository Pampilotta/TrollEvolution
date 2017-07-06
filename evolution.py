from generation import Generation
from troll import Troll
class Evolution():
 
 """   An Evolution-Object drives the evol procedure by processing   """
 """   generations in order to hit the goal by recombinations.       """
 def __init__(self, generation):
    self.goal = generation.goal
    self.parentGeneration = generation.parentGeneration
    self.newGeneration = generation.newGeneration
    self.possibleAttributes = generation.possibleAttributes
    self.evolutionFinish = False
    self.doEvolve()
 
 def doEvolve(self):
    while not self.evolutionFinish:
        for j in range(100000):
            for i in range(12):
                if self.newGeneration[i] == self.goal:
                    reqTroll = self.newGeneration[i]
                    print("The requested Troll was born!")
                    print("fix me: name is missing " + str(reqTroll.look) + str(reqTroll.sex))
                    self.evolutionFinisch = True
        
            evolGeneration = Generation(self.newGeneration, self.goal, self.possibleAttributes)     
            self.generation = evolGeneration.sortTrolls()
        self.evolutionFinish = True
