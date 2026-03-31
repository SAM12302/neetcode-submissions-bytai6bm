class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        count = 1
        max = 1
        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                count += 1
                if count > max:
                    return True
            my_dict[nums[i]] = count
        return False