class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Используем кучу для поиска k самых близких точек.
        # В качестве ключа для сравнения берем квадрат расстояния (x^2 + y^2),
        # так как это проще и быстрее, чем считать корни.
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)