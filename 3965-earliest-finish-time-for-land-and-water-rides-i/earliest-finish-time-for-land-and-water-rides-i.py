class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        ans = float('inf')
        for i in range(n):
            for j in range(m):
                t1 = landStartTime[i] + landDuration[i]
                t2 = max(waterStartTime[j], t1) + waterDuration[j]
                ans = min(ans, t2)

        for i in range(n):
            for j in range(m):
                t1 = waterStartTime[j] + waterDuration[j]
                t2 = max(landStartTime[i], t1) + landDuration[i]
                ans = min(ans, t2)
        return ans