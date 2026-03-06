import random

# --- ФУНКЦИИ ---
def partition_lomuto(arr, low, high):
    """
    Процедура разделения массива по схеме Ломуто.
    Опорный элемент (pivot) помещается на свою итоговую отсортированную позицию.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    """
    Рандомизация опорного элемента для защиты от худшего случая.
    """
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition_lomuto(arr, low, high)

def quick_select_recursive(arr, low, high, k):
    """
    Рекурсивная функция поиска k-го элемента.
    """
    # Базовый случай: если массив сузился до одного элемента
    if low == high:
        return arr[low]

    # Разделяем массив и получаем точный индекс опорного элемента
    pivot_index = randomized_partition(arr, low, high)

    # ПОЧЕМУ АЛГОРИТМ НЕ СОРТИРУЕТ ВЕСЬ МАССИВ:
    # Здесь происходит отсечение лишней работы. В отличие от QuickSort,
    # мы идем только в ту сторону, где гарантированно находится индекс k.
    # Это снижает количество операций, так как вторая половина массива просто игнорируется.
    if k == pivot_index:
        # Элемент найден
        return arr[k]
    elif k < pivot_index:
        # Искомый элемент находится в левой части
        return quick_select_recursive(arr, low, pivot_index - 1, k)
    else:
        # Искомый элемент находится в правой части
        return quick_select_recursive(arr, pivot_index + 1, high, k)

def quick_select(arr, k):
    """
    Обертка для запуска QuickSelect с проверкой границ.
    """
    if not 0 <= k < len(arr):
        return "Ошибка: k вне диапазона"
    
    # Передаем копию массива (arr[:]), чтобы не изменять исходный массив,
    # так как partition модифицирует элементы in-place.
    return quick_select_recursive(arr[:], 0, len(arr) - 1, k)

# --- ЗАПУСК ---
if __name__ == "__main__":
    print("=== ЗАПУСК QUICKSELECT ===")
    try:
        raw_input = input("Введите массив чисел через пробел: ")
        if raw_input.strip():
            arr = list(map(int, raw_input.split()))

            k_input = input(f"Введите k (индекс от 0 до {len(arr)-1}): ")
            k = int(k_input)

            print(f"\nМассив: {arr}")
            print(f"Ищем элемент с индексом k={k} (это {k+1}-й наименьший элемент)")

            result = quick_select(arr, k)

            print(f"Результат: {result}")
        else:
            print("Массив пуст.")

    except ValueError:
        print("Ошибка ввода (проверьте, что вводите числа).")
