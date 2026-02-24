class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Используем список как кучу
        heap = []
        
        for num in nums:
            # Добавляем текущее число в кучу
            heapq.heappush(heap, num)
            
            # Если в куче стало больше k элементов,
            # убираем самый маленький из них (верхушку)
            if len(heap) > k:
                heapq.heappop(heap)
                
        # В куче осталось ровно k самых больших чисел.
        # Самое маленькое из них (верхушка) — это k-й максимум.
        return heap[0]