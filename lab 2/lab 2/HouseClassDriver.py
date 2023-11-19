from HouseClass import House

class HouseDriver:
    """
    Клас, який використовується для демонстрації функціоналу класу House.
    """

    def __init__(self):
        """
        Конструктор класу HouseDriver.
        Створює об'єкт класу House для тестування.
        """
        self.house = House()  # Створюємо об'єкт класу House для тестування

    def run_demo(self):
        """
        Метод, який демонструє роботу класу House.
        """
        print("Демонстрація роботи класу House:")
        # Будуємо будинок
        self.house.build_house("Вулиця Шевченка, 123", 3)

        # Додаємо поверхи
        self.house.add_floor()
        self.house.add_floor()

        # Поселяємо жильців
        self.house.add_citizen("Іванов Іван")
        self.house.add_citizen("Петров Петро")

        # Показуємо інформацію про будинок
        self.house.show_info()

        # Змінюємо фасад будинку
        self.house.design_house("Модерністичний фасад")

        # Показуємо оновлену інформацію про будинок
        self.house.show_info()

        # Виселяємо жильця
        self.house.remove_citizen("Іванов Іван")

        # Виселяємо всіх жильців
        self.house.remove_all_citizens()

        # Видаляємо будинок
        self.house.remove_house()

        # Спроба видалення поверху з пустого будинку
        self.house.remove_floor()

        # Спроба додавання жильця до знищеного будинку
        self.house.add_citizen("Новий житель")

        # Показуємо інформацію про будинок (повинна бути порожня)
        self.house.show_info()
