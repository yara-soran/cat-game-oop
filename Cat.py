# Our Cat Entity
class Cat:
    # The constructor:
    # - The constructor wll create a cat for us in code.
    # - To create a cat we need given_name and given_colour.
    # - Self is the cat we are creating.
    def __init__(self, given_name, given_colour):
        # Name attribute.
        self.name = given_name
        # Colour attribute.
        self.colour= given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5

    def train(self):
        print(f"{self.name} is training...")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1

    def feed(self):
        print(f"{self.name} is eating...")
        self.energy += 10
        self.weight += 1
        self.age += 0.1


# We will now make 2 cats.
# Each one is an instance of the Cat class.
sid = Cat("Sid", "Black")
mista = Cat("Mista", "White")
sid.train()
print(sid.intelligence)
print(mista.intelligence)