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
    evolGeneration = Generation(self.parentGeneration, self.goal, self.possibleAttributes)
    while not self.evolutionFinish:
        survivors = evolGeneration.sortTrolls()
        evolGeneration = Generation(survivors, self.goal, self.possibleAttributes)
        for Troll in survivors:
            if (Troll.look == self.goal.look) and (Troll.sex == self.goal.sex): 
                print("The requested Troll was born!")
                print("fix me: name is missing " + str(Troll.look) + str(Troll.sex))
                self.evolutionFinish = True
                break
    
