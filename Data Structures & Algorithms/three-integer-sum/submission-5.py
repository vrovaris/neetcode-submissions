class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        seen = set()

        for i in range(len(nums)):
            target = -nums[i]

            left, right = 0, len(nums) - 1

            
            while (left < right):              

                if left == i:
                    left += 1
                    continue

                if right == i:
                    right -= 1
                    continue
                
                if (nums[left] + nums[right] == target and 
                tuple(sorted([nums[i], nums[left], nums[right]])) not in seen):

                    ans.append([nums[i], nums[left], nums[right]])
                    seen.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                    

                elif (nums[left] + nums[right] > target):
                    right -= 1
                else:
                    left += 1


        return ans
        # -nums[i] = nums[j] + nums[k] 
        #  [-2, 0, 1, 1, 2]