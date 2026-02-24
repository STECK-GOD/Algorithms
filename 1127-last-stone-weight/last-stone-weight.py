class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python имеет только min-heap. Чтобы имитировать max-heap,
        # делаем все числа отрицательными. Теперь -8 < -1, поэтому -8 будет на вершине.
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        # Пока в куче больше одного камня, продолжаем "бить" их
        while len(max_heap) > 1:
            # Достаем самый тяжелый (самый маленький отрицательный)
            stone1 = -heapq.heappop(max_heap)
            # Достаем второй по тяжести
            stone2 = -heapq.heappop(max_heap)
            
            # Если они не равны, добавляем остаток обратно
            if stone1 != stone2:
                new_stone = stone1 - stone2
                heapq.heappush(max_heap, -new_stone)
                
        # Возвращаем последний камень (с положительным знаком) или 0, если куча пуста
        return -max_heap[0] if max_heap else 0