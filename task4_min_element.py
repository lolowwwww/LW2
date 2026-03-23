import random

def get_matrix():
    print("\n--- Задача 4: Минимальный элемент матрицы ---")
    choice = input("Хотите сгенерировать данные автоматически? (да/нет): ").lower()
    
    if choice in ['да', 'y', 'yes', '']:
        rows = random.randint(3, 5)
        cols = random.randint(3, 5)
        print(f"Генерация матрицы размером {rows}x{cols}...")
        matrix = [[random.randint(-50, 50) for _ in range(cols)] for _ in range(rows)]
        return matrix
    else:
        print("Введите количество строк (N) и столбцов (M):")
        try:
            n = int(input("N (строки) = "))
            m = int(input("M (столбцы) = "))
            matrix = []
            print(f"Введите {n} строк по {m} чисел:")
            for i in range(n):
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода!")
            return get_matrix()

def print_matrix(matrix):
    for row in matrix:
        print(row)

def find_min_element(matrix):
    if not matrix or not matrix[0]:
        return None, None, None
        
    min_val = matrix[0][0]
    min_row = 0
    min_col = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_row = i
                min_col = j
                
    return min_val, min_row, min_col

if __name__ == "__main__":
    matrix = get_matrix()
    if matrix:
        print("\nВаша матрица:")
        print_matrix(matrix)
        
        min_val, r_idx, c_idx = find_min_element(matrix)
        
        print(f"\nМинимальный элемент: {min_val}")
        # Индексы выводим с 0 (как в программировании) или с 1 (как в математике). 
        # Здесь выведем как в программировании [row][col]
        print(f"Его индексы: строка {r_idx}, столбец {c_idx} (нумерация с 0)")
        print(f"Позиция в матрице: [{r_idx}][{c_idx}]")