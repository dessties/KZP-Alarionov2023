import math

class ExpressionCalculator:
    def calculate_expression(self, x):
        try:
            result = math.tan(x) / (1 / math.tan(x))
            return result
        except ZeroDivisionError:
            print("Ділення на нуль. Результат невизначений для цього значення x.")

# Створення екземпляру класу та виклик методу calculate_expression
calculator = ExpressionCalculator()
x_value = 0  # Задайте значення x
result = calculator.calculate_expression(x_value)
print(f"Результат виразу при x = {x_value} є: {result}")
