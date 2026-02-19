class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Ставим указатели на концы массивов с реальными числами
        p1 = m - 1
        p2 = n - 1
        # Указатель на самый конец nums1 (где стоят нули)
        p = m + n - 1
        
        # Пока во втором массиве есть что переносить
        while p2 >= 0:
            # Если в первом массиве еще есть числа и они больше
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Иначе берем число из второго массива
                nums1[p] = nums2[p2]
                p2 -= 1
            
            # Сдвигаем указатель вставки
            p -= 1