matrix = []
while True:
    row = input("Введите строку матрицы (Enter для завершения): ").strip()
    if not row:
        break
    numbers = [int(x.strip()) for x in row.split(',')]
    if matrix and len(numbers) != len(matrix[0]):
        print("Ошибка: все строки должны быть одинаковой длины.")
        continue
    matrix.append(numbers)

print("Введите вторую матрицу:")
matrix2 = []
while True:
    row = input("Введите строку матрицы (Enter для завершения): ").strip()
    if not row:
        break
    numbers = [int(x.strip()) for x in row.split(',')]
    if matrix2 and len(numbers) != len(matrix2[0]):
        print("Ошибка: все строки должны быть одинаковой длины.")
        continue
    matrix2.append(numbers)

if len(matrix) == len(matrix2) and len(matrix[0]) == len(matrix2[0]):
    result_add = [[matrix[i][j] + matrix2[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    print("Сложение матриц:")
    for row in result_add:
        print(row)
else:
    print("Ошибка: размеры матриц не совпадают.")

num = int(input("Введите число для умножения: "))
result_mult_num = [[element * num for element in row] for row in matrix]
print("Умножение первой матрицы на число:")
for row in result_mult_num:
    print(row)

if len(matrix[0]) == len(matrix2):
    result_mult = [[sum(matrix[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix))]
    print("Умножение матриц:")
    for row in result_mult:
        print(row)
else:
    print("Ошибка: количество столбцов первой матрицы не равно числу строк второй матрицы.")
