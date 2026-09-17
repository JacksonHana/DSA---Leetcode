class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # # print(nums)
        # sum = 0
        # for i in range(0,len(nums),2):
        #     sum += nums[i]
        # return sum

        # nums.sort()
        # print(nums)
        # pair = []
        # for i in range(0, len(nums), 2):
        #     # if (i + 1) < len(nums):
        #         pair.append((nums[i], nums[i+1]))
        # print(pair)
        # sum = 0
        # for i in pair:
        #     sum += min(i)

        # return sum

        # nums.sort()
        # print(nums)
        # slicing
        # print(nums[::2])
        # print(sorted(nums))
        return (sum(sorted(nums)[::2]))
