class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sort_list = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return sort_list[:k]