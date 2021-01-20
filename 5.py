class Stationery:

    def __init__(self, name):
        self.name = name

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Ручка рисует")


class Pencil(Stationery):

    def draw(self):
        print("Карандаш рисует")


class Handle(Stationery):

    def draw(self):
        print("Маркер рисует")


mel = Stationery('mel')
mel.draw()
pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()

