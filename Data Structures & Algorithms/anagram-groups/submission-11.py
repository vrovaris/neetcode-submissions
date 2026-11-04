class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} # sorted_str : list[]

        for string in strs: 
            sort = "".join(sorted(string))

            # sort = 

            if sort in hash_map:
                hash_map[sort].append(string)

            else: 
                hash_map[sort] = [string]
            

        return list(hash_map.values())

