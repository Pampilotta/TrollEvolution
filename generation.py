from random import randrange
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
     
     lookChild = self.mutate(lookChild)
     
     randomParentsPicker = randrange(0,2)
     sexChild = parents[randomParentsPicker].sex
     
     return [parents, Troll(lookChild, sexChild)]

 """   Adds a random Attribute from the possible Attributes with a   """
 """   given propability                                             """
 def mutate(self, lookChild):
     posArea = randrange(0, 3)
     posAttribute = randrange(0, 3)
     newAttribute = 1 
     lookChild[posArea][posAttribute] = self.possibleAttributes[newAttribute]
     
     return lookChild

 """   A method, that produces 12 new Trolls by using the mixingDNA  """
 """   -mehtod. All random produced Trolls are returned in no order  """
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
        tmp = tmp/9
        sim.append([tmp, trollsToProof[i]])
        tmp = 0
        
    return sim

 """   A method, that devides the old and the new Generation into    """
 """   two Gererations: a valid and a invalid                        """
 def sortTrolls(self):
     validTrolls = []
     invalidTrolls = []
     newTrolls = self.similarity(self.newGeneration)
     oldTrolls = self.similarity(self.parentGeneration)
     
     
     for i in range(6):
         comp = []
         locMax = max(newTrolls, key=lambda item: item[0])
         validTrolls.append(locMax[1])
         newTrolls.remove(locMax)
    
     for i in range(6):
         locMax = max(oldTrolls, key=lambda item: item[0])
         validTrolls.append(locMax[1])
         oldTrolls.remove(locMax)
         
     while len(newTrolls) != 0:
         while len(oldTrolls) != 0:
             invalidTrolls.append(oldTrolls[0][1])
             del oldTrolls[0]
         invalidTrolls.append(newTrolls[0][1])
         del newTrolls[0]
    
     print("Following Trolls were discarded: ")
     for i in range(len(invalidTrolls)):
         print(str(invalidTrolls[i].look) + ",  " + str(invalidTrolls[i].sex))
     
    
     print("\n")
     
     print ("Valid Trolls are: ")
     for i in range(len(validTrolls)):
         print(str(validTrolls[i].look) + ",  " + str(validTrolls[i].sex))
    
     return validTrolls
         
