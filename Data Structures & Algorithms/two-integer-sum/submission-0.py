class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in seen:  
                ans = []
                if (i < seen[diff]):
                    ans.append(i)
                    ans.append(seen[diff])
                else:
                    ans.append(seen[diff])
                    ans.append(i)
                return ans
            else:
                seen[num] = i