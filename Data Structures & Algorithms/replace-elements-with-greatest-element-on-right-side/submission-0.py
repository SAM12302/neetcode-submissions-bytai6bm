class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        myList = arr.copy()
        max = -1
        for i in range(len(arr)):
            print(f"Ith element: {myList[i]}")
            max = -1
            for j in range(i + 1, len(arr)):
                print(f"Jth element: {myList[j]}")
                if myList[j] > max:
                    max = myList[j]
                    print("Maximum = ", max)
            myList[i] = max
        return myList