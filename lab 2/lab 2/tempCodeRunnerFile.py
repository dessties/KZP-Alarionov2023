import sys
from HouseClassDriver import HouseDriver

class CustomLogger:
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        with open(self.filename, 'a') as file:
            file.write(message)

# Встановлюємо вивід у файл
log_filename = 'output.log'
sys.stdout = CustomLogger(log_filename)

# Викликаємо метод run_demo() та виводимо результат у файл
driver = HouseDriver()
driver.run_demo()

# Повертаємо стандартний вивід на консоль
sys.stdout = sys.__stdout__


driver = HouseDriver()
driver.run_demo()