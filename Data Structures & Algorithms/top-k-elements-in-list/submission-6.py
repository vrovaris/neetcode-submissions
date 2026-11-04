class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        size = len(nums) + 1
        buckets = [[] for _ in range(size)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for item, frequency in freq.items():
            buckets[frequency].append(item)
        
        ans = []
        for cur_list in reversed(buckets): 
            if cur_list: 
                for item in cur_list:
                    ans.append(item)
                    if len(ans) == k:
                        return ans 
