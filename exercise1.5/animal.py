class Animal (object):
    def __init__(self, age):
        self.age = age
        self.name = None

    # Getter methods for age and name
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    # Setter methods
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # Well-formatted string representation
    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + "\nAge: " + str(self.age)
        return output
    
class Cat(Animal):
    # Introducing a new method where it speaks
    def speak(self):
        print("Meow")

    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + "\nAge: " + str(self.age)
        return output
    
class Dog(Animal):
    def speak(self):
        print("Woof!")

    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + "\nAge: " + str(self.age)
        return output
    
class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)

        self.set_name(name)

        self.friends = []

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def show_friends(self):
        for friend in self.friends:
            print(friend)

    def speak(self):
        print("Hello, my name's " + self.name + "!")

    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output