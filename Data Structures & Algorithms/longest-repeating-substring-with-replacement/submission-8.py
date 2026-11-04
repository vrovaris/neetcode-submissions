class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        result = 0 

        for right in range(len(s)):
            window_len = right - left + 1
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(freq.values())

            while (window_len - max_freq > k): 
                freq[s[left]] -= 1
                left += 1

                window_len = right - left + 1
                max_freq = max(freq.values())


            result = max(window_len, result)
        return result