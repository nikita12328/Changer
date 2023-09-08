from task1.my_classes.Animal import Animal


class Fish(Animal):
    def __init__(self, weight: int, height: int, pet: bool, species: str):
        super().__init__(weight, height, pet)
        self.__species = species

    @staticmethod
    def move(**kwargs):
        print("I am swimming")

    def get_species(self):
        return self.__species


if __name__ == '__main__':
    fish1 = Fish(10, 20, True, "Окунь")
    fish1.move()
    print(fish1.get_species())
