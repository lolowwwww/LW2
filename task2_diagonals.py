import random

def get_matrix():
    print("\n--- Задача 2: Сумма диагоналей матрицы ---")
    choice = input("Хотите сгенерировать данные автоматически? (да/нет): ").lower()
    
    if choice in ['да', 'y', 'yes', '']:
        n = random.randint(3, 5) # Размер матрицы от 3x3 до 5x5
        print(f"Генерация квадратной матрицы размером {n}x{n}...")
        matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
        return matrix
    else:
        print("Введите размер матрицы N (так как нужны диагонали, матрица будет NxN):")
        try:
            n = int(input("N = "))
            matrix = []
            print(f"Введите {n} строк матрицы (числа через пробел):")
            for i in range(n):
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: в строке должно быть {n} элементов!")
                    return get_matrix()
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода!")
            return get_matrix()

def print_matrix(matrix):
    for row in matrix:
        print(row)

def calculate_diagonals(matrix):
    n = len(matrix)
    main_diag_sum = 0
    secondary_diag_sum = 0
    
    for i in range(n):
        main_diag_sum += matrix[i][i]
        secondary_diag_sum += matrix[i][n - 1 - i]
        
    return main_diag_sum, secondary_diag_sum

if __name__ == "__main__":
    matrix = get_matrix()
    if matrix:
        print("\nВаша матрица:")
        print_matrix(matrix)
        
        main_sum, sec_sum = calculate_diagonals(matrix)
        print(f"\nСумма элементов главной диагонали: {main_sum}")
        print(f"Сумма элементов побочной диагонали: {sec_sum}")