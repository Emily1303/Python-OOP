class Mammal:

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
        self.__species = 'animals'

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__species

    def info(self):
        return f'{self.name} is of type {self.type}'


animal = Mammal('Maria', 'dog', 'borf-borf')
print(animal.make_sound())
print(animal.get_kingdom())
print(animal.info())
