class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 1. Функция "просеивания" элемента вниз. 
        # Она толкает число вниз по дереву, пока оно не станет больше своих детей.
        def sift_down(start, end):
            root = start
            while True:
                child = 2 * root + 1 # Левый ребенок
                if child > end: break
                
                # Если есть правый ребенок и он больше левого — выбираем его
                if child + 1 <= end and nums[child] < nums[child + 1]:
                    child += 1
                
                # Если ребенок больше родителя — меняем их местами
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child # Продолжаем проверку для этого числа ниже
                else:
                    break # Число на своем месте, выходим

        # 2. Построение кучи (Heapify). 
        # Превращаем массив в дерево, где сверху — самое большое число.
        # Начинаем с последнего родителя и идем к началу.
        for start in range((n - 2) // 2, -1, -1):
            sift_down(start, n - 1)

        # 3. Сама сортировка.
        # Берем самое большое число (индекс 0), меняем его с последним.
        # "Забываем" про последний элемент и чиним дерево для оставшихся.
        for end in range(n - 1, 0, -1):
            nums[end], nums[0] = nums[0], nums[end]
            sift_down(0, end - 1)
            
        return nums