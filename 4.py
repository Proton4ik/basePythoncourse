class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Автомобиль {} начал движение".format(self.name))

    def stop(self):
        print("Автомобиль {} остановился".format(self.name))

    def turn(self, direction):
        self.direction = direction
        print("Автомобиль {} повернул {}".format(self.name, self.direction))

    def show_speed(self):
        print("Скорость автомобиля {} равна {}".format(self.name, self.speed))


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Скорость автомобиля {} равна {}, превышение скорости!!!".format(self.name, self.speed))
        else:
            print("Скорость автомобиля {} равна {}".format(self.name, self.speed))


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Скорость автомобиля равна {}, превышение скорости!!!".format(self.name, self.speed))
        else:
            print("Скорость автомобиля {} равна {}".format(self.name, self.speed))


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


lexus = TownCar(70, "black", "Лексус", False)
lexus.show_speed()
lexus.go()
lexus.turn('налево')
lexus.stop()
mazda = SportCar(180, "white", "Mazda", False)
mazda.show_speed()
mazda.go()
mazda.turn('налево')
mazda.stop()
ford = PoliceCar(50, "blue", "Ford", True)
print(ford.is_police)
kamaz = WorkCar(40, "yellow", "KAMAZ", False)
kamaz.show_speed()
