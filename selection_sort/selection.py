def selection_sort(arr):
    n = len(arr)
    
    # Проходим по всему массиву
    for i in range(n):
        # Предполагаем, что текущий элемент (i) — минимальный
        min_idx = i
        
        # Ищем реальный минимум в оставшейся части массива
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Если найденный минимум не стоит на своем месте, меняем их
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

# Блок запуска программы (UI)
if __name__ == "__main__":
    print("--- СОРТИРОВКА ВЫБОРОМ ---")
    try:
        # Ввод данных пользователем
        user_input = input("Введите числа через пробел: ")
        
        # Преобразование строки в список чисел
        data = list(map(int, user_input.split()))
        
        print(f"Исходный массив: {data}")
        
        # Выполнение сортировки
        selection_sort(data)
        
        print(f"Отсортированный: {data}")
        print("----------------------------")
    except ValueError:
        print("Ошибка: введите корректные целые числа через пробел.")
