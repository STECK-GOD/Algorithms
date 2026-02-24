class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Сортируем массив от меньшего к большему
        nums.sort()
        
        # Берем k-й элемент с конца
        # Например, если k=1, это самый последний (самый большой)
        return nums[-k]