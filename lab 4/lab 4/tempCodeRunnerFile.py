import math

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

calculator = ExpressionCalculator()
x_value = 0
result = calculator.calculate_expression(x_value)
print(f'Результат при х = {x_value}: {result}')