class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Множество для отслеживания уникальных элементов
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
