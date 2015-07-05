class Animal:
	def __init__(self, name, age, weight)
	self.name = name
	self.age = age
	self.weight = weight
	def eat(self):
		self.weight += 1


class Panda(Animal):
    def _init_(self, name, age, weight):
    	'''self.name = name
    	self.age = age
    	self.__weight = weight'''
    	super().__init_(name, age, weight)
    	self.skill =  skill

    def __eg__(self, other):
    	return self.name == other.name

    def __str__(self):
    	return self.name + " " + str(self.age)

    def eat(self): #self- za da ima dostup do chlen pandite
        self.__weight += 10
        print(" NOM NOM NOM ")

    def _sleep(self):
    	self.__weight +=10

    def __set_name(self):
    	self.name= name

'''
ivan = Panda("Ivan", 20, 200) # vrushta konkretna instanciq, obekt
ivan.__weight = 5000
print(ivan)
pesho= Panda("Ivan", 5, 150)
ivan= Panda("Ivan", 5, 200)
print(pesho == ivan)
'''
panda = Panda("Ivan", 10, 200, 10)
panda.eat()




class Panda: 
	def __init__(self):
		self._dna = 'pandish'
		