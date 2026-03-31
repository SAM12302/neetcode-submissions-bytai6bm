class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        max = 1
        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
            if my_dict[nums[i]] > max:
                return True
        return False