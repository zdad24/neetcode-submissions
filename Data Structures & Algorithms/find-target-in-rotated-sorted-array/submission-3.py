class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            #left sorted portion
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1  # target is in left sorted portion
                else:
                    l = mid + 1  # target is in right portion
                    
            #right sorted portion
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1  # target is in right sorted portion
                else:
                    r = mid - 1  # target is in left portion
                    
        return -1