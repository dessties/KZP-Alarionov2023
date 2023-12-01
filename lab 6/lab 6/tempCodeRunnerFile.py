class PencilCase:
    def __init__(self):
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

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

    @classmethod
    def create_with_items(cls, *args):
        pencil_case = cls()
        for item in args:
            pencil_case.add_item(item)
        return pencil_case

# Приклад використання параметризованого класу "Пенал"
pen_case = PencilCase.create_with_items(5, 10, 3, 7)

pen_case.view_items()  # Виведе всі елементи у пеналі

pen_case.find_min_item()  # Знайде та виведе найменший елемент у пеналі

pen_case.remove_item(3)  # Видалить елемент з пенала

pen_case.view_items()  # Виведе оновлений зміст пенала
