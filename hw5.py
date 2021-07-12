import dataclasses
from collections import namedtuple


################1################
class Laptop:
    def __init__(self):
        firm = Battery('HP')
        capacity = Battery('5h')
        self.battery = [firm, capacity]


class Battery:
    def __init__(self, energy):
        self.energy = energy


laptop = Laptop()


################2################
class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self):
        pass


string = GuitarString()


################3################
class Calc:
    def __init__(self):
        pass

    @staticmethod
    def add_nums(x1, x2, x3):
        return x1 + x2 + x3


print(Calc.add_nums(7, 5, 11))


################4################
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza ({self.ingredients})'

    @classmethod
    def carbonara(cls, ingredient):
        s = ['forcemeat', 'tomatoes']
        return cls(s)

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


print(Pasta.carbonara(''))
p1 = Pasta([''])
print(p1.bolognaise())


################5################
class Concert:
    max_visitors_num = 50

    def __init__(self):
        self.visitors_count = 0

    @property
    def visitors_count(self):
        return f'{self._visitors_count}'

    @visitors_count.setter
    def visitors_count(self, visitor_count):
        if visitor_count > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitor_count


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)


################6################
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


record = AddressBookDataClass(1, 'Daria Plokhotniuk', '0951234567', 'Odesa', 'daria@mail.com', '18.10.2000', 20)
record_dict = {'key': 2,
                'name': 'Rostyslav Kitsylinksyy',
                'phone_number': '090123456678',
                'address': 'Lviv',
                'email': 'rostyslav@mail.com',
                'birthday': '12.05.1998',
                'age': 23}

print(record.name)
print(record.address)
print(record_dict['birthday'])
print(record_dict['age'])


################7################
AddressBookDataClass = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

record = AddressBookDataClass(1, 'Daria Plokhotniuk', '0951234567', 'Odesa', 'daria@mail.com', '18.10.2000', 20)

print(record[4])
print(record.phone_number)


################8################
class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{AddressBook.__name__} key: {self.key}, " \
               f"name:'{self.name}', phone_number:'{self.phone_number}', " \
               f"address:'{self.address}', email:'{self.email}', " \
               f"birthday:'{self.birthday}', age:{self.age}"


my_address = AddressBook(1, 'Daria Plokhotniuk', '0951234567', 'Odesa', 'daria@mail.com', '18.10.2000', 20)
print(str(my_address))


################9################
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def full_name(self):
        return f'{self.name} {self.surname} {self.age}'


anna = Person('Anna', 'Tech', 20)
anna.age = 16
print(anna.age)


################10################
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


dasha = Student
setattr(dasha, "email", "dasha@mail.com")
setattr(dasha, "student_email", "cursor@mail.com")
print(getattr(dasha, "student_email",))


################11################
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def convert(self):
        result = (self._temperature * 1.8) + 32
        return f'{result}'


obj = Celsius()
obj._temperature = 17
print(f'{obj._temperature} C = {obj.convert} F')