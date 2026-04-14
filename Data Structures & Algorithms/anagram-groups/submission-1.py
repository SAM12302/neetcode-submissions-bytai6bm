class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        result = []
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in a:
                a[word_sorted] = []
            a[word_sorted].append(word)

        for index, key in enumerate(a):
            result.append(a[key])

        return result
