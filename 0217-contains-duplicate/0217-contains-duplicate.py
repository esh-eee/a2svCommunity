class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = 1 + dic.get(nums[i], 0)

        for key, val in dic.items():
            if val > 1:
                return True

        return False