#index      0  1  2  3  4  5  6  7  8  9
#nums       0  0  1  1  1  2  2  3  3  4
#update     0  1  1  2
#slow                s
#fast                      f
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            else: fast += 1

        return slow +1
