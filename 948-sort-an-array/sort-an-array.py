class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Вспомогательная функция для просеивания (восстановления свойства кучи)
        def heapify(n, i):
            largest = i          # Изначально считаем корень самым большим
            left = 2 * i + 1     # Индекс левого потомка
            right = 2 * i + 2    # Индекс правого потомка
            
            # Если левый потомок существует и он больше корня
            if left < n and nums[left] > nums[largest]:
                largest = left
                
            # Если правый потомок существует и он больше текущего максимума
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            # Если самый большой элемент не корень, меняем их местами
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                # Рекурсивно просеиваем дальше
                heapify(n, largest)

        n = len(nums)
        
        # 1. Построение Max-Heap (максимальной кучи)
        # Идем с середины массива к началу
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
            
        # 2. Извлекаем элементы из кучи по одному
        for i in range(n - 1, 0, -1):
            # Перемещаем текущий корень (он же самый большой элемент) в самый конец
            nums[i], nums[0] = nums[0], nums[i]
            # Восстанавливаем кучу для оставшейся части массива
            heapify(i, 0)
            
        return nums