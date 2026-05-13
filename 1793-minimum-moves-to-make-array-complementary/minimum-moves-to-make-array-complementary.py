class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Difference array for sums from 2 to 2k
        diff = [0] * (2 * k + 2)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Boundary values for 1-move range
            low = min(a, b) + 1
            high = max(a, b) + k
            sum_ab = a + b
            
            # Step 1: Default to 2 moves for all sums in [2, 2k]
            diff[2] += 2
            diff[2 * k + 1] -= 2
            
            # Step 2: Reduce to 1 move for the range [low, high]
            diff[low] -= 1
            diff[high + 1] += 1
            
            # Step 3: Reduce to 0 moves for the specific point sum_ab
            diff[sum_ab] -= 1
            diff[sum_ab + 1] += 1
            
        # Sweep across the difference array to find the minimum
        min_moves = n # Max possible moves is n
        current_moves = 0
        for i in range(2, 2 * k + 1):
            current_moves += diff[i]
            min_moves = min(min_moves, current_moves)
            
        return min_moves