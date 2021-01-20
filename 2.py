class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self):
        m = (self._length * self._width * 25 * 5) / 1000
        print("Масса асфальта для создания данной дороги составляет {:.2f} тонн ".format(m))


length_road = float(input("Введите длину дороги в метрах: "))
width_road = float(input("Введите ширину дороги в метрах: "))
first_road = Road(length_road, width_road)
first_road.count()
