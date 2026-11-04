class Solution:

    def countFrequencies(self, string: str) -> List:
        ans = [0] * 26
        norm = ord('a')

        for char in string:
            ans[ord(char) - norm] += 1

        return tuple(ans)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} 

        for string in strs: 
            sort = self.countFrequencies(string)

            if sort in hash_map:
                hash_map[sort].append(string)

            else: 
                hash_map[sort] = [string]
            
        return list(hash_map.values())