class Body:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person(Body):
    def __init__(self, name, age, height):
        Body.__init__(self,name, age)
        self.height = height
guy = Person("james",13,199)
print(guy.name)
print(guy.height)