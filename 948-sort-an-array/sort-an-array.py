class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def sift_down(start, end):
            root = start
            while True:
                child = 2 * root + 1
                if child > end: 
                    break
                if child + 1 <= end and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break
        for start in range((n - 2) // 2, -1, -1):
            sift_down(start, n - 1)
        for end in range(n - 1, 0, -1):
            nums[end], nums[0] = nums[0], nums[end]
            sift_down(0, end - 1)
            
        return nums
import sys
input = sys.stdin.read