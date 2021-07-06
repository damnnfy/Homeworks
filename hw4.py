#########1###############
class Vehicle:
        def __init__(self, max_speed, mileage):
            self.max_speed = max_speed
            self.mileage = mileage

        def get_info(self):
         print(f'This vehicle max speed is {self.max_speed} and miliage is {self.mileage}')


Bike = Vehicle(100, 25000)
print(Bike.get_info())


#########2##########
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def get_number(self):
        print(f'There are {self.seating_capacity} sits')


Double_decker = Bus(140, 250000, 150)
print(Double_decker.get_info())
print(Double_decker.get_number())

############3#########
print(type(Double_decker))
###############4#########
check = isinstance(Double_decker, Vehicle)
print(check)


##################5#########
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        print(f'ID of school is {self.school_id}')

    def get_number_of_students(self):
            print(f'Number is {self.number_of_students}')


School_1 = School(1, 5000)
print(School_1.get_school_id())
print(School_1.get_number_of_students())


####################6##########
class SchoolBus(Bus, School):
    def __init__(self, school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        School.__init__(self, school_id, number_of_students)
        self.bus_school_color = bus_school_color

    def get_color(self):
        print(f'Color is {self.bus_school_color}')


Bus_1 = SchoolBus(1, 5000, 140, 250000, 150, 'yellow')
print(Bus_1.get_info())
print(Bus_1.get_school_id())
print(Bus_1.get_number_of_students())
print(Bus_1.get_number())
print(Bus_1.get_color())


####################7##########
class Bear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a bear and my name is {self.name} and I am {self.age} years old.')

    def make_sound(self):
        print('RRR')

class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
     print(f'I am a wolf and my name is {self.name} and I am {self.age} years old.')

    def make_sound(self):
     print('WOOO')


bear = Bear('Ivan', 3)
wolf = Wolf('Rex', 5)


for animal in (bear, wolf):
 animal.info()
 animal.make_sound()


############8############


