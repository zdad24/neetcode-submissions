class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        prefix = []

        postfix = []
        ans = 1
        for i in range(len(nums)):
            ans *= nums[i]
            prefix.append(ans)

        ans = 1
        for i in range(len(nums)-1, -1, -1):
            ans *= nums[i]
            postfix.append(ans)

        postfix = postfix[::-1]

        for i in range(len(nums)):
            if i == 0:
                ans = 1 * postfix[i+1]
                result.append(ans)
            elif i == len(nums)-1:
                ans = prefix[i-1] * 1
                result.append(ans)
            else:
                ans = prefix[i-1] * postfix[i+1]
                result.append(ans)
        return result