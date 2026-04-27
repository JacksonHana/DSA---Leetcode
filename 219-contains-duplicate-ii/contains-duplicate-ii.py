class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i,n in enumerate(nums):
            if n in hashmap and abs(i - hashmap[n]) <= k:
                return True
            hashmap[n] = i
        return False