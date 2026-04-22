class Animal:
    all_animals = []
    kingdom = "Animalia"

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.all_animals.append(self)

    def speak(self):
        print("The animal makes a noise.")

    def __str__(self):
        return f"Kingdom: 'Animalia', Name: '{self.name}', Species: '{self.species}'"