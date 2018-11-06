from car import Car
from person import Person 


pam = Person("Pam Beasley", "Secretary")
# chrysler = Car("Chrysler", "Sebring Convertible", 2004, "Michael Scott")

datsun = Car("Datsun", "280Z", 1978, {'name': "Dwight Schrute", 'occupation': "Paper Salesperson", 'favotite_tv_show': "Battlestar Galactica"})
toyota = Car("Toyota", "Yaris", 2007, pam)


michael = Person("Michael Scott", "Regional Manager")
sebring = Car("Chrysler", "Sebring Convertible", 2004, michael)
dwight = Person("Dwight Schrute", "Paper Salesperson")
datsun.owner = dwight
# let's create more people
meredith = Person("Meredith Palmer", "Purchaser - Supplier Relations")
ford_minivan = Car("Ford", "Aerostar Minivan", 1997, meredith)
jim = Person("Jim Halpert", "Paper Salesperson")
corolla = Car("Toyota", "Corolla", 2000, jim)
stanley = Person("Stanley Hudson", "Paper Salesperson")
camry = Car ("Toyota", "Camry", 2008, stanley)



