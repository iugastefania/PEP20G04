class CarFactory():

    """ class that produces an given amount of cars and puts into a dictonary in values a list of 3 elements: the day, serial number , lot number
    Class CarFactory is a class that stores the serial and lot numbers of a given number of produced cars in a certain day
     Attributes:
    day: the given date
    start: the starting serial number from where to begin to produce more cars
    number: the number of cars to be produced
    dictionar: used to keep track of car serial and lot numbers produced in a certain day

    Methods:
    adauga: fills the dictionary with data from the given number of produced cars
    rightside: returns the serial number of rightside cars
    leftside: returns the serial number of leftside cars
    iter, next: iterating the object will return the lot numbers produced that day
    """

    index = 0
    k = 0

    def __init__(self, day:int, start:int, number:int, dictionar = {}):
        """start is the starting serial number, number is the number of how many cars need to be produced, dictionar is the place where we keep them

         Parameters
        ----------:
         day: the given date
         start: the starting serial number from where to begin to produce more cars
          number: the number of cars to be produced
          dictionar: used to keep track of car serial and lot numbers produced in a certain day
        """

        self.start = start
        self.day = day
        self.number = number
        self.dictionar = dictionar
        self.start2 = start

    def adauga(self):
        """ index keeps count of how many cars produced out of the given number, fills the dictionary with data from the given number of produced cars
        fills the dictionary with data from the given number of produced cars
        the index par counts the producing of the cars so there will be the exact number given of cars produced
         the start par is incremented with each car produced
           the lot number of the each car is the serial number of each car // 20
         the values of the dictionary are lists of 3 that keep : the day, the serial number and the lot number
           the dictionary is returned after producing cars
           Parameters
            ----------:
           index: to count the number of already produced cars
        """

        while self.index < self.number:

            self.dictionar[self.index] = [self.day, self.start, self.start//20]
            self.start += 1
            self.index += 1

        return self.dictionar

    def rightside(self):
        """ right side cars have odd serial number , we return the cars that have rightside """

        for x, y, z in self.dictionar.values():
            if y % 2 == 1:
                print(y, end=',')

    def leftside(self):
        """ left side cars have even serial number, we return the cars that have leftside """

        for x, y, z in self.dictionar.values():
            if y % 2 == 0:
                print(y, end=',')

    def __iter__(self):
        return self

    def __next__(self):
        """iterating the object will return the lot numbers produced that day"""

        if self.k > self.number:
            raise StopIteration

        result = self.start2 // 20

        self.start2 += 1
        self.k += 1

        return result

masina = CarFactory(10,111,91)
print(masina.adauga())

print('rightside:')
masina.rightside()
print()

print('\nleftside:')
masina.leftside()
print()

file = open('my_text', mode='w')

for x in masina:
    file.write(str(x))
    file.write('\n')

file.close()
print()