import math
import pickle

class ExpressionCalculator:
    def calculate_expression(self, x):
        try:
            result = math.tan(x) / (1 / math.tan(x))
            return result
        except ZeroDivisionError:
            print("Ділення на нуль. Результат невизначений для цього значення x.")
            return None
        except Exception as e:
            print(f"Виникла помилка: {e}")
            return None

class ResultSaver:
    @staticmethod
    def save_text(result, filename):
        with open(filename + ".txt", "w") as file:
            file.write(str(result))

    @staticmethod
    def save_binary(result, filename):
        with open(filename + ".pkl", "wb") as file:
            pickle.dump(result, file)

    @staticmethod
    def read_text(filename):
        with open(filename + ".txt", "r") as file:
            return file.read()

    @staticmethod
    def read_binary(filename):
        with open(filename + ".pkl", "rb") as file:
            return pickle.load(file)

# Приклад використання
calculator = ExpressionCalculator()
x_value = 1
result = calculator.calculate_expression(x_value)

# Збереження результату в обох форматах
ResultSaver.save_text(result, "result_text")
ResultSaver.save_binary(result, "result_binary")

# Читання результатів
text_result = ResultSaver.read_text("result_text")
binary_result = ResultSaver.read_binary("result_binary")

print(f"Текстовий результат: {text_result}")
print(f"Двійковий результат: {binary_result}")
