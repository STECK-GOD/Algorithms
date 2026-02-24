class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        # Преобразуем список в кучу
        heapq.heapify(self.heap)
        
        # Если чисел больше чем k, убираем лишние (самые маленькие),
        # пока не останется ровно k элементов
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Добавляем новое значение в кучу
        heapq.heappush(self.heap, val)
        
        # Если размер кучи превысил k, удаляем самый маленький элемент
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # Возвращаем верхушку кучи — это и есть k-й максимум
        return self.heap[0]