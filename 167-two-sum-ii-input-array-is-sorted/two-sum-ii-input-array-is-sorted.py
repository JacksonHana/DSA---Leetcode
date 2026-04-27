class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in hashmap: # check n in hashmap
                return [hashmap[diff] , i+1]
            hashmap[n] = i+1


        # # Solution 2 pointers
        # i, j = 0, len(numbers)-1
        # while i < j:
        #     if numbers[i] + numbers[j] > target:
        #         j -= 1
        #     elif numbers[i] + numbers[j] < target:
        #         i += 1
        #     else: # num[i] == num[j]
        #         return (i+1, j+1)