from abc import ABC, abstractmethod


class Store(ABC):
    length = 50
    width = 70
    height = 3
    devices_list = ['Printer', {}, 'Scanner', {}, 'Xerox', {}]

    def __init__(self, model, quantity):
        self.model = model
        self.quantity = quantity

    @abstractmethod
    def get(self, model, quantity):
        pass


class Device(ABC):
    printers = {}
    scanners = {}
    xeroxes = {}

    def __init__(self, model, color):
        self.model = model
        self.color = color

    @abstractmethod
    def give(self, department, quantity: int):
        pass


class Printer(Device, Store):
    list_per_min = 50

    def get(self, model, quantity: int):
        self.model = model
        self.quantity = quantity
        Store.devices_list[1].update({self.model: self.quantity})

    def give(self, department, quantity: int):
        self.department = department
        self.quantity = quantity
        Device.printers.update({self.department: self.quantity})
        Store.devices_list[1].update({self.model: self.quantity})


class Scan(Device, Store):
    list_per_min = 25

    def get(self, model, quantity: int):
        self.model = model
        self.quantity = quantity
        Store.devices_list[3].update({self.model: self.quantity})

    def give(self, department, quantity: int):
        self.department = department
        self.quantity = quantity
        Device.scanners.update({self.department: self.quantity})


class Xerox(Device, Store):
    list_per_min = 15

    def get(self, model, quantity: int):
        self.model = model
        self.quantity = quantity
        Store.devices_list[5].update({self.model: self.quantity})

    def give(self, department, quantity: int):
        self.department = department
        self.quantity = quantity
        Device.xeroxes.update({self.department: self.quantity})


p = Printer('Canon', 'red')
s = Scan('hp', 'blue')
x = Xerox('Xerox', 'black')
p.get('Canon', 500)
p.give('IT', 20)
p.give('Finance', 30)
s.get('hp', 500)
s.give('IT', 20)
s.give('Finance', 30)
x.get('Xerox', 500)
x.give('IT', 20)
x.give('Finance', 30)
print(Store.devices_list)
print(Device.printers, Device.scanners, Device.xeroxes)

