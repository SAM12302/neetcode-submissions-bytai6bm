class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        s_list = list(s)
        for i in range(len(s_list) - 1):
            score += abs(ord(s_list[i]) - ord(s_list[i + 1]))
        return score