class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_letters_s = {}
        seen_letters_t = {}

        for i in range(len(s)):
            letter = s[i]
            if letter not in seen_letters_s:
                seen_letters_s[letter] = 1

            else:
                seen_letters_s[letter] += 1

        for i in range(len(t)):
            letter = t[i]
            if letter not in seen_letters_t:
                seen_letters_t[letter] = 1

            else:
                seen_letters_t[letter] += 1

        return seen_letters_s == seen_letters_t