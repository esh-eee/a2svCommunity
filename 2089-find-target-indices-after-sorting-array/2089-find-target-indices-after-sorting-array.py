class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targetIndexes = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                targetIndexes.append(i)
                
        return targetIndexes
    