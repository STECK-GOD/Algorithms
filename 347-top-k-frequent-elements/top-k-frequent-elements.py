class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Считаем частоту каждого элемента
        # Counter создает словарь вида {элемент: частота}
        count = Counter(nums)
        
        # Используем кучу для получения k самых частых элементов
        # nlargest берет k элементов, ключом сравнения служит их частота (count.get)
        return heapq.nlargest(k, count.keys(), key=count.get)