class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if target == nums[i] + nums[j]:
                        a.append(i)
                        a.append(j)
                        return a
                        