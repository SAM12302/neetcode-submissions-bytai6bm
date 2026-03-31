class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        myList = arr.copy()
        max = -1
        for i in range(len(arr)):
            max = -1
            for j in range(i + 1, len(arr)):
                if myList[j] > max:
                    max = myList[j]
            myList[i] = max
        return myList