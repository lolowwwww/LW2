import random

def get_data():
    print("\n--- Задача 1: Сортировка последовательности ---")
    choice = input("Хотите сгенерировать данные автоматически? (да/нет): ").lower()
    
    if choice in ['да', 'y', 'yes', '']:
        # Генерация случайного списка из 10 чисел от 1 до 100
        data = [random.randint(1, 100) for _ in range(10)]
        print(f"Сгенерированный список: {data}")
        return data
    else:
        # Ручной ввод
        print("Введите числа через пробел:")
        try:
            user_input = input("> ")
            data = list(map(int, user_input.split()))
            return data
        except ValueError:
            print("Ошибка ввода! Вводите только целые числа.")
            return get_data()

def sort_sequence(data):
    # Используем встроенный метод сортировки (Timsort)
    # Если нужно реализовать алгоритм вручную (например, пузырьком), раскомментируйте код ниже:
    """
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
    """
    return sorted(data)

if __name__ == "__main__":
    data = get_data()
    if data:
        sorted_data = sort_sequence(data)
        print(f"Отсортированный список: {sorted_data}")