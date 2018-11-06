# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
    	return self._name
    
    @property
    def occupation(self):
    	return self._occupation

    @classmethod
    def has_oldest_car(cls):
    	car_year = {}
    	for car in Car._all: 
    		car_year[car] = car.year
    	return min(car_year, key=car_year.get).owner

    @classmethod
    def drives_a(cls, make):
    	owners = []
    	for car in Car._all: 
    		if car.make == make: 
    			owners.append(car.owner)
    	return owners 

    def drives_same_make_as_me(self):
    	owners = []
    	my_car = list(filter(lambda car: car.owner == self, Car._all))[0]
    	same_makes = filter(lambda car: car.make == my_car.make and car.owner != self, Car._all)
    	return list(map(lambda car: car.owner, same_makes))

    	# for car in Car._all: 
    	# 	if car.make == self.
 
    	




    	# find all cars with dates
    	# find lowest date
    	# owner from that car 

    

