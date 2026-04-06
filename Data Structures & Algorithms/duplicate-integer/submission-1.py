class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for num in nums:
            if nums.count(num) > 1 and num not in dup:
                dup.append(num)

        return bool(dup)
         