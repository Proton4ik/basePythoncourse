from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    def count(self):
        c = (self.size/6.5) + 0.5
        return round(c)


class Smoking(Clothes):
    def count(self):
        return (2 * self.size + 0.3)/ 100


coat = Coat(58)
smoking = Smoking(185)
print(coat.count() + smoking.count())

