class Solution:
    def isValid(self, s: str) -> bool:
        inverse_map = {"{" : "}", "(" : ")", "[" : "]"}
        stack = []

        for item in s: 
            if item in inverse_map.keys():
                stack.append(item)
            elif len(stack) == 0 or item != inverse_map[stack.pop()]:
                return False

        return len(stack) == 0
