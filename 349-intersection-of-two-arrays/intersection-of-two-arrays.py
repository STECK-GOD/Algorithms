class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Преобразуем массивы во множества
        set1 = set(nums1)
        set2 = set(nums2)

        # Операция пересечения множеств
        return list(set1 & set2)
