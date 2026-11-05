class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {}

        for char_s, char_t in zip(s,t): 
            freqS[char_s] = freqS.get(char_s, 0) + 1
            freqT[char_t] = freqT.get(char_t, 0) + 1

        return freqS == freqT    