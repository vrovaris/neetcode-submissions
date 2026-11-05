class Solution:

    # freq --> tuple() : Array of strings that map to this list  

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for string in strs: 
            
            arr = [0] * 26
            for char in string:
                arr[ord(char) - ord('a')] += 1
            
            arr = tuple(arr)
            if arr in freq:
                freq[arr].append(string)
            else:
                freq[arr] = [string]
            

        return list(freq.values())