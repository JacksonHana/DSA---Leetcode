#index  0  1  2  3  4  5
#nums   1  2  1
#ans    1  -  -  1

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] *2*n
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans