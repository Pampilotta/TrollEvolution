from troll import Troll
from generation import Generation
from evolution import Evolution
from random import shuffle

"""   Creating randomly some attributes for the first Generation     """
"""   and the goal-Troll, which causes success.                      """
looksOfMales = []
looksOfFemales = []
lookOfGoal= [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
goal = Troll(lookOfGoal, "f")

"""   Every Generation has 12 Trolls                                 """
for i in range(12): 
	
	head = [ i for i in range(1,4)]
	shuffle(head)

	body = [ i for i in range(1,4)]
	shuffle(body)

	legs = [ i for i in range(1,4)]
	shuffle(legs)
	
	if i <= 5 :
		looksOfMales.append([head, body, legs])
		
	else:
		looksOfFemales.append([head, body, legs])

"""   Instanciating first Generation of Trolls                       """
possibleAttributes = range(1, 4)
firstGeneration = []

while len(looksOfMales) != 0:
		firstGeneration.append(Troll(looksOfMales[0], "m"))
		del looksOfMales[0]

while len(looksOfFemales) != 0:
		firstGeneration.append(Troll(looksOfFemales[0], "f"))
		del looksOfFemales[0]

print("Goal: " + str(goal.look) + " Sex: " + str(goal.sex))
for i in range(len(firstGeneration)):
	print(str(i+1) + "   : " + str(firstGeneration[i].look) + "      " +str(firstGeneration[i].sex))

"""   Starting a evolution process by first generation               """
testGen = Generation(firstGeneration, goal, possibleAttributes)
evolutionProcess = Evolution(testGen)

