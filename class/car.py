class Car:
    def __init__(self, color, model, door_number):
        self.color = color
        self.model = model
        self.door_number = door_number

    def print_info(self):
        print("цвет :", self.color)
        print("модель :", self.model)
        print("количетсво дверей :", self.door_number)

print("CAR_1")
car_1 = Car("желтый", door_number = 4, model = "lada")
car_1.print_info()

print()
print("CAR_2")
car_2 = Car("Черный", "УАЗ", 9)
car_2.print_info()