import time


class TrafficLight:

    __color = "pulse yellow"

    def running(self):
        while True:
            self.__color = "red"
            if self.__color != "red":
                print("Ошибка в работе светофора. Мигающий Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break
            print("Красный! Будет гореть 7 секунд")
            print(self.__color)
            time.sleep(7)
            self.__color = "yellow"
            if self.__color != "yellow":
                print("Ошибка в работе светофора. Мигающий Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break
            print("Желтый! Будет гореть 2 секунды")
            print(self.__color)
            time.sleep(2)
            self.__color = "green"
            if self.__color != "green":
                print("Ошибка в работе светофора. Мигающий Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break
            print("Зеленый! Будет гореть 5 секунд")
            print(self.__color)
            time.sleep(5)
            working = input("Если хотите выключить светофор введите q: ")
            if working == "q":
                print("Мигает Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break


light_switcher = TrafficLight()
light_switcher.running()
