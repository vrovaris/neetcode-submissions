class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        total = 1
        total_without_zero = 1
        zeroes = 0

        for num in nums:            
            total *= num
            if num != 0:
                total_without_zero *= num
            else:
                zeroes += 1

            if zeroes > 1: 
                total_without_zero = 0 
            
            
        # print(total)
        # print(total_without_zero)

        for num in nums:
            if num != 0:
                ans.append(total // num)
            else: 
                ans.append(total_without_zero)

        return ans
