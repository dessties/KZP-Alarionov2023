class PencilCase:
    def __init__(self):
        self.contents = []

    def add_item(self, number, item):
        self.contents.append(item)
        self.contents.append(number)

    def remove_item(self, item):
        if item in self.contents:
            self.contents.remove(item)
        else:
            print(f"{item} не знайдено у пеналі.")

    def view_items(self):
        if self.contents:
            print("Зміст пенала:")
            for item in self.contents:
                print(item)
        else:
            print("Пенал порожній.")

    def find_min_item(self):
        if self.contents:
            min_item = min(self.contents)
            print(f"Мінімальний елемент у пеналі: {min_item}")
            return min_item
        else:
            print("Пенал порожній. Немає мінімального елементу.")

# Приклад використання класу "Пенал"
pen_case = PencilCase()

pen_case.add_item(5, "ручка")
pen_case.add_item(10)
pen_case.add_item(3)
pen_case.add_item(7)

pen_case.view_items()  # Виведе всі елементи у пеналі

pen_case.find_min_item()  # Знайде та виведе найменший елемент у пеналі

pen_case.remove_item(3)  # Видалить елемент з пенала

pen_case.view_items()  # Виведе оновлений зміст пенала
