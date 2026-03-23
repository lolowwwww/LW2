import random

def get_matrix():
    print("\n--- Задача 3: Определитель матрицы ---")
    choice = input("Хотите сгенерировать данные автоматически? (да/нет): ").lower()
    
    if choice in ['да', 'y', 'yes', '']:
        n = random.randint(2, 4) 
        print(f"Генерация матрицы размером {n}x{n}...")
        # Генерируем числа с плавающей точкой для интереса, или целые
        matrix = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
        return matrix
    else:
        print("Введите размер матрицы N:")
        try:
            n = int(input("N = "))
            matrix = []
            print(f"Введите {n} строк матрицы:")
            for i in range(n):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                matrix.append(row)
            return matrix
        except ValueError:
            print("Ошибка ввода!")
            return get_matrix()

def print_matrix(matrix):
    for row in matrix:
        # Форматируем вывод, чтобы было красиво
        print("[ " + " ".join(f"{x:6.2f}" for x in row) + " ]")

def determinant(matrix):
    n = len(matrix)
    # Создаем копию, чтобы не менять исходную
    mat = [row[:] for row in matrix]
    det = 1.0
    
    for i in range(n):
        # Поиск ведущего элемента
        pivot = i
        while pivot < n and mat[pivot][i] == 0:
            pivot += 1
            
        if pivot == n:
            return 0.0 # Определитель равен 0
        
        if pivot != i:
            # Меняем строки местами
            mat[i], mat[pivot] = mat[pivot], mat[i]
            det *= -1 # При перестановке строк знак меняется
            
        det *= mat[i][i]
        
        # Обнуление элементов ниже ведущего
        for j in range(i + 1, n):
            factor = mat[j][i] / mat[i][i]
            for k in range(i, n):
                mat[j][k] -= factor * mat[i][k]
                
    return det

if __name__ == "__main__":
    matrix = get_matrix()
    if matrix:
        print("\nВаша матрица:")
        print_matrix(matrix)
        
        det = determinant(matrix)
        print(f"\nОпределитель матрицы: {det:.2f}")