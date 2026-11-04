import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        res = []

        for num in nums: 
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for item, frequency in freq.items(): 
            res.append((frequency, item))
        
        res.sort(key=lambda x: (x[0], x[1]))
        ans = []
        for i in range(k):
            ans.append(res.pop()[1])

        return ans

        


