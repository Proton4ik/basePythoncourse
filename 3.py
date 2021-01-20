class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print("Полное имя сотрудника: ", self.name, self.surname)

    def get_total_income(self):
        print("Суммарный доход: ", int(self._income.get("wage") + self._income.get("bonus")))


worker1 = Position("Леша", "Lesha", "Proger", 10000, 5000)
print(worker1.name, worker1.surname, worker1.position, worker1._income)
worker1.get_full_name()
worker1.get_total_income()
