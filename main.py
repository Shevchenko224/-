
   car_count = 0
def __init__(self, make, model, year, color, speed=0):

 self.make = make

self.model = model

self.year = year
self.color = color

self.speed = speed



Car.car_count += 1

def start(self):

       self.speed = 10
def accelerate(self, amount):

 self.speed += amount

def stop(self):

       self.speed = 0

car1 = Car("Toyota", "Camry", 2020, "сірий")

car2 = Car("Honda", "Civic", 2019, "червоний")

car1.start()

car1.accelerate(30)

car2.start()

car2.accelerate(20)

car2.stop()

print("Кількість автомобілів:", Car.car_count)

