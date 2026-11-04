class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0
        for num in nums:

            if ((num - 1) in seen):
                continue

            curr_seq_longest = 1

            while (num + curr_seq_longest in seen):
                curr_seq_longest += 1

            longest = max(curr_seq_longest, longest)
            
        return longest
                