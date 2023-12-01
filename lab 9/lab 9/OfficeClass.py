from HouseClass import House

class Office(House):
    def office_functionality(self, employee_count):
        """
        Реалізація методу з абстрактного класу House.
        """
        print(f"Додаткові функціональності офісу. Кількість працівників: {employee_count}")