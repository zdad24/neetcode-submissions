class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        result = []
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                result = [i, seen.get(target - nums[i])]
            else:
                seen[nums[i]] = i

        return sorted(result)