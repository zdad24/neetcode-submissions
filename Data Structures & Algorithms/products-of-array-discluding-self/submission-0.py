class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)): 
            mul = 1
            for j in range(len(nums)):
                if not i == j:
                    mul *= nums[j]
            result.append(mul)

        return result