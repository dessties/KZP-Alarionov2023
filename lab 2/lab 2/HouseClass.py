class House:
    """
    Клас, який представляє будинок.
    """

    def __init__(self, address="", floors=0, citizens=None, facade="Звичайний фасад"):
        """
        Конструктор класу House.

        :param address: Адреса будинку.
        :param floors: Кількість поверхів у будинку.
        :param citizens: Список жильців у будинку.
        :param facade: Тип фасаду будинку.
        """
        self.address = address
        self.floors = floors
        self.citizens = citizens if citizens is not None else []
        self.facade = facade



    def build_house(self, address, floors):
        """
        Метод, який створює будинок.

        :param address: Адреса будинку.
        :param floors: Кількість поверхів у будинку.
        """
        self.address = address
        self.floors = floors
        print(f"Будинок на адресі {self.address} з {self.floors} поверхами був успішно збудований.")

    def remove_house(self):
        """
        Метод, який знищує будинок.
        """
        print(f"Будинок на адресі {self.address} був знищений.")
        self.address = ""
        self.floors = 0
        self.citizens = []

    def add_floor(self):
        """
        Метод, який додає поверх до будинку.
        """
        self.floors += 1
        print(f"Додано новий поверх. Загальна кількість поверхів: {self.floors}")

    def remove_floor(self):
        """
        Метод, який деінсталює поверх будинку.
        """
        if self.floors > 1:
            self.floors -= 1
            print(f"Останній поверх був видалений. Загальна кількість поверхів: {self.floors}")
        else:
            print("Будинок не може існувати без поверхів")

    def add_citizen(self, citizen_name):
        """
        Метод, який поселяє жильця на поверх.

        :param citizen_name: Ім'я жильця.
        """
        self.citizens.append(citizen_name)
        print(f"{citizen_name} був поселений у будинку.")

    def remove_citizen(self, citizen_name):
        """
        Метод, який виселяє жильця.

        :param citizen_name: Ім'я жильця.
        """
        if citizen_name in self.citizens:
            self.citizens.remove(citizen_name)
            print(f"{citizen_name} був виселений з будинку.")
        else:
            print(f"{citizen_name} не знайдений у будинку.")

    def give_address(self):
        """
        Метод, який повертає адресу будинку.

        :return: Адреса будинку.
        """
        return self.address

    def remove_all_citizens(self):
        """
        Метод, який виселяє всіх жильців.
        """
        self.citizens.clear()
        print("Всі жильці були виселені.")

    def show_info(self):
        """
        Метод, який показує інформацію про будинок.
        """
        print(f"Адреса будинку: {self.address}")
        print(f"Кількість поверхів: {self.floors}")
        print(f"Список жильців: {', '.join(self.citizens)}")
        print(f"Фасад будинку: {self.facade}")

    def design_house(self, new_facade):
        """
        Метод, який змінює фасад будинку.

        :param new_facade: Новий тип фасаду будинку.
        """
        self.facade = new_facade
        print(f"Фасад будинку був змінений на: {self.facade}")
