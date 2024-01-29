class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_dog(self):
        print(self.name + "'s", "age is", self.age, "and weight is", self.weight)

    def bark(self):
        if self.weight > 29:
            print(self.name, "says WOOF WOOF")
        else:
            print(self.name, "says woof woof")

    def human_years(self):
        years = self.age * 7
        return years

    def __str__(self):
        return "I'm a dog named " + self.name


class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = False

    def walk(self):
        print(self.name, "is helping its handler", self.handler, "walk")

    def bark(self):
        if self.is_working:
            print(self.name, "says, \"I can't bark, I'm working\"")
        else:
            Dog.bark(self)


codie = Dog("Codie", 12, 38)
jackson = Dog("Jackson", 9, 12)
rody = ServiceDog("Rody", 8, 38, "Joseph")

print(codie)
print(jackson)
print(rody)
rody.bark()
rody.is_working = True
rody.walk()
