from random import randrange
import random
from random import choice
from troll import Troll
class Generation():
    
 """   A Generation-Object. Every Generation has 12 Trolls and is    """
 """   produced randomly, but selected by the strongest              """
 def __init__(self, parentGeneration, goal, possibleAttributes):
    self.parentGeneration = parentGeneration
    self.goal = goal
    self.possibleAttributes = possibleAttributes
    self.newGeneration = self.produceGeneration()

 """   A method, that chooses randomly two parents from the parent-  """
 """   generation. It returns a List-object with two (f/m) parents.  """    
 def chooseParents(self):
    randomIndex = randrange(0, len(self.parentGeneration))
    mother = self.parentGeneration[randomIndex]
	 
    while mother.sex != "f" :
        randomIndex = randrange(0, len(self.parentGeneration))
        mother = self.parentGeneration[randomIndex]

    randomIndex = randrange(0, len(self.parentGeneration))
    father = self.parentGeneration[randomIndex]
      
    while father.sex != "m" :
        randomIndex = randrange(0, len(self.parentGeneration))
        father = self.parentGeneration[randomIndex]
    
    return [mother, father]

 """   A method, that mixes the parents attributes randomly and re-  """
 """   turns a List-object with the parents and their child          """
 def mixingDNA(self):
     parents = self.chooseParents()
     lookChild = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
     
     for i in range(3):
         for j in range(3):
             randomParentsPicker = randrange(0,2)
             lookParent= parents[randomParentsPicker].look
             lookChild[i][j] = lookParent[i][j]
     
     mutationRange = range(1, 101)
     mutationModul = 20
     randIndex = random.choice(mutationRange)
     
     if (randIndex % mutationModul) == 0:
         lookChild = self.mutate(lookChild)
     
     randomParentsPicker = randrange(0,2)
     sexChild = parents[randomParentsPicker].sex
     
     return [parents, Troll(lookChild, sexChild)]

 """   Adds a random Attribute from the possible Attributes with a   """
 """   given propability                                             """
 def mutate(self, lookChild):
     print("MUTATION: from / to\n" + str(lookChild))  
     posArea = randrange(0, 3)
     posAttribute = randrange(0, 3)
     newAttribute = randrange(0, 3) 
     lookChild[posArea][posAttribute] = self.possibleAttributes[newAttribute]
     
     print(str(lookChild))
     return lookChild

 """   A method, that produces 12 new Trolls by using the mixingDNA  """
 """   -method. All random produced Trolls are returned in no order  """
 def produceGeneration(self):
    tmpRes = []
    childTrolls = []
    parentsOfChildren = []
    
    for i in range(12):
        tmpRes = self.mixingDNA()
        childTrolls.append(tmpRes[1])
        parentsOfChildren.append(tmpRes[0])
        
    return childTrolls

 """   A method, that detects the similarity between every Troll in  """
 """   the trollsToProof-Generation and the given self.goal-Troll    """
 def similarity(self, trollsToProof):
    sim = []
    tmp = 0
    troll = []
    for i in range(len(trollsToProof)):
        troll = trollsToProof[i]
        for j in range(3):
            for k in range(3):
                tmp = tmp + (self.goal.look[j][k]/troll.look[j][k])
        tmp = int((tmp/9)*10**6)
        sim.append((tmp, trollsToProof[i]))
        tmp = 0
    
    """print("Method 'similarity': #Keys = " + str(len(sim.keys())) + " #Values = " + str(len(sim.values())))"""
    return sim

 """   A method, that devides the old and the new Generation into    """
 """   two Gererations: a valid and a invalid                        """
 def sortTrolls(self):
     validTrolls = []
     invalidTrolls = []
     newTrolls = self.similarity(self.newGeneration)
     betwixtGeneration = self.similarity(self.parentGeneration)
     
     while len(newTrolls) != 0:
         betwixtGeneration.append(newTrolls.pop())     
     
     sortedTrolls = sorted(betwixtGeneration, key = lambda tup : tup[0])
     for i in range(len(sortedTrolls)):
         print(str(i) + ". Sorted Trolls: " + str(sortedTrolls[i][0]))
    
     j = len(sortedTrolls)-1
     for i in range(int(len(sortedTrolls)/2)):
         print("Valid hinzugefügt: " + str(sortedTrolls[j][0]))
         validTrolls.append(sortedTrolls[j][1])
         j = j-1
                 
     while j >= 0:
         print("                               Invalid hinzugefügt: " + str(sortedTrolls[j][0]))
         invalidTrolls.append(sortedTrolls[j][1])
         j = j-1

     return validTrolls
         
