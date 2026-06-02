class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost_sr = sorted(cost)
        n = len(cost)
        total = 0
        for i in range(n-1, -1, -3):
            total += cost_sr[i]
            if i-1 >= 0:
                total += cost_sr[i-1]
            
        return total