# Создайте три (или более) отдельных классов животных.
# Например, рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.



class Animal:
    def __init__(self, weight, height, pet):
        self.weight = weight
        self.height = height
        self.pet = pet

    def move(self):
        print("I am moving")