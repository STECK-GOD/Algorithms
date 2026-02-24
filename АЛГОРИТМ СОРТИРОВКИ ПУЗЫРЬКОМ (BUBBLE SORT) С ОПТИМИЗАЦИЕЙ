def bubble_sort(arr):
    n = len(arr)
    # Внешний цикл отвечает за проходы
    for i in range(n):
        swapped = False
        
        # Внутренний цикл сравнивает соседние элементы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Оптимизация: если перестановок не было, выходим
        if not swapped:
            break
    return arr

# Блок запуска программы (UI)
if __name__ == "__main__":
    print("--- СОРТИРОВКА ПУЗЫРЬКОМ ---")
    try:
        # Ввод данных пользователем
        user_input = input("Введите числа через пробел: ")
        
        # Преобразование строки в список чисел
        data = list(map(int, user_input.split()))
        
        print(f"Исходный массив: {data}")
        
        # Выполнение сортировки
        bubble_sort(data)
        
        print(f"Отсортированный: {data}")
        print("-----------------------------")
    except ValueError:
        print("Ошибка: введите корректные целые числа через пробел.")
