class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Hello my name is {self.name} and I am {self.age} y/o")

    def speak(self):
        print(
            'This "speak" fuction will be overwritten if the class being used has a fuction with the same name'
        )


class Dog(Pets):
    def speak(self):
        print("Bark")


class Cat(Pets):
    def __init__(self, name, age, color):
        # super() is how you call the parent class and fetch the arguments from it (In this case the arguments from the __init__ fuction)
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(
            f"Hello my name is {self.name} and I am {self.age} y/o. I am {self.color} colored"
        )


class Fish(Pets):
    pass


p1 = Dog("Ellie", 7)
p2 = Cat("Luna", 2, "Tortise Shell")
p3 = Fish("Fush", 12)

p1.speak()
p2.show()
p3.speak()
