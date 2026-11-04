class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set()
        longest = 1
        
        if not nums:
            return 0

        for num in nums:
            seen.add(num)

        for num in nums:

            if ((num - 1) in seen):
                continue

            curr_seq_longest = 1
            num += 1

            while (num in seen):
                curr_seq_longest += 1
                num += 1

            if (curr_seq_longest > longest):
                longest = curr_seq_longest

        return longest
                