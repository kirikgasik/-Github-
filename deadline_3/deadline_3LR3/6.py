class SmartLight:
    def __init__(self, brightness=50, color="white"):
        self.brightness = brightness  
        self.color = color            
        self.__is_on = False 
    def turn_on(self):
        self.__is_on = True
        print(f"Лампочка включена. Яркость: {self.brightness}%, Цвет: {self.color}")
    def turn_off(self):
        self.__is_on = False
        print("Лампочка выключена")
    def set_color(self, new_color):
        if self.__is_on:
            self.color = new_color
            print(f"Цвет изменен на: {new_color}")
        else:
            print("Ошибка: сначала включите лампочку!")
    def get_status(self):
        status = "включена" if self.__is_on else "выключена"
        return f"Статус: {status}, Яркость: {self.brightness}%, Цвет: {self.color}"
print()
lamp2 = SmartLight()  
print(f"Начальные параметры: Яркость={lamp2.brightness}%, Цвет={lamp2.color}")
lamp2.turn_on()
lamp2.set_color("теплый белый")
lamp2.brightness = 30  
print(lamp2.get_status())