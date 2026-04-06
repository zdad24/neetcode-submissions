class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = 1000
        while (l<=r):
            mid = (r+l)//2
            if (nums[mid] >= nums[l]):
                res = min(res, nums[l])
                l=mid+1
            else:
                res = min(res, nums[mid])
                r=mid-1

        return res



        