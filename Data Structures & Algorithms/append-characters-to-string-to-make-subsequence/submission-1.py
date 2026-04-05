class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        count = 0
        for character in s:
            if i < len(t):
                if t[i] == character:
                    count += 1
                    i += 1
        remaining = len(t[(count):])
        return remaining
