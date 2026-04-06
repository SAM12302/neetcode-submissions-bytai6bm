class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        previous_count = 0
        for character in reversed(s):
            previous_count = count
            if character == " ":
                count = 0
            else:
                count += 1
            if previous_count > 0 and count == 0:
                return previous_count
        return count
        

