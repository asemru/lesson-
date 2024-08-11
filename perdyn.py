class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
       num = 1
       if new_floor > self.number_of_floors:
           print(f"это не логично, всего этажей - {self.number_of_floors}, нужный этаж - {new_floor}")
       else:
           while num < new_floor:
               print(num)
               num += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and other.number_of_floors == self.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors < other.number_of_floors or (other.number_of_floors == self.number_of_floors and self.number_of_floors == other.number_of_floors)

    def __ge__(self, other):
        return self.number_of_floors > other.number_of_floors or (other.number_of_floors == self.number_of_floors and self.number_of_floors == other.number_of_floors)

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors and other.number_of_floors != self.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self.number_of_floors

    def __radd__(self, value):
        return self.number_of_floors - value

    def __del__(self):
        print(f"{self.name} снесён, но останется в истории")

#h1 = House("Пупкин", number_of_floors=20)
#h2 = House("Васёк", number_of_floors=5)



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)



del h2
del h3

print(House.houses_history)


#print(h1)
#print(h2)
#print(h1 < h2)
#print(h1 == h2, h2 == h1)
#print(h1 > h2)
#print(h1 <= h2)
#print(h1 >= h2)
#print(h1 != h2)
#h1 = h1 + 10
#h2 += 10
#print(h1, h2)
#print(House.houses_history)
#del h2
#del h1
#print(House.houses_history)

#__str__
#print(h1)
#print(h2)

#__len__
#print(len(h1))
#print(len(h2))
