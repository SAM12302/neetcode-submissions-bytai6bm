class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        i = 0
        if s and t is not None:
            for character in t:
                if i < len(s):
                    if s[i] == character:
                        count += 1
                        i += 1
                else:
                    break
            if count == len(s):
                return True
            else:
                return False
        else:
            return True