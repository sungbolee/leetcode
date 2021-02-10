from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(0, len(nums)):
            print(i)
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out


a = Solution()
print(a.productExceptSelf([1, 2, 3, 4]))
