class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for character in reversed(s.strip()):
            if character == " ":
                break
            else:
                count += 1
        return count
        

