class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = min(nums[l], nums[r])

        while (l < r):
            
            mid = (l + r) // 2
            ans = min(nums[l], nums[r], nums[mid], ans)
            if nums[l] <= nums[mid]: 
                l = mid + 1
            else:
                r = mid

        return ans    