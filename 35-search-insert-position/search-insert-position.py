class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid # если нашли число - сразу возвращаем индекс
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            # В этом вся соль: если цикл закончился и число не найдено -
        # left указывает именно туда, где число должно стоять.
        return left