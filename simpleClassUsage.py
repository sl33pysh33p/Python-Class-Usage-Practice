class person:
    def __init__(self, name, age):
        """
        Args:
            __init__ : upon initialisation, get these args
            name : gets name
            age : gets age
        """

        self.name = name
        self.age = age

    def get_name(self):
        # gets name from __init__ function
        return self.name

    def get_age(self):
        # gets age from __init__ function
        return self.age

    def set_age(self, age):
        # modify age from the originally set one with an arg in the set_age function
        self.age = age
        return self.age


# define p as having the class of person, and setting the __init__ args
p = person("Tom", 16)


# uses p variable and uses functions get_name and get_age from inside the person class to fetch: Name and age. Then prints name and age.
print(p.get_name(), p.get_age())


# uses p variable and set_age function from person class, to change the arg of age from what it was initially set to.
print(p.set_age(35))
