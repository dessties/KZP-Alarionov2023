import numpy as np

def generate_array():
    size = int(input('Введіть розмір квадратної матриці: '))
    filler = input('Введіть символ-заповнювач масиву: ')

    if size <= 0 or len(filler) != 1:
        print('Некоректні дані. Робота програми перервана.')
        return

    matrix = np.full((size, size), ' ')

    for i in range(size):
        for j in range(size):
            if j >= size - i:
                matrix[i][j] = filler

    print('Згенерований масив:')
    for row in matrix:
        print(' '.join(row))

    output_string = '\n'.join([' '.join(row) for row in matrix])
    with open('output.txt', 'w') as file:
        file.write(output_string)

    print('Масив також збережено у файлі "output.txt".')

if __name__ == "__main__":
    generate_array()
