class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums) 
        # Если общая сумма нечетная, поделить поровну на целые числа нельзя
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        # dp[i] скажет нам, реально ли собрать сумму i из наших чисел
        dp = [False] * (target + 1)
        dp[0] = True # Сумму 0 можно собрать всегда (не беря ничего)     
        for num in nums:
            # Проходим по таблице справа налево, чтобы не использовать одно и то же
            # число дважды для одной и той же суммы (как в 0/1 Knapsack)
            for i in range(target, num - 1, -1):
                # Если мы уже могли собрать сумму i или можем собрать i-num
                dp[i] = dp[i] or dp[i - num]       
        return dp[target]