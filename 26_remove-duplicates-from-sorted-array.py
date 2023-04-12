from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


example = Solution()
res = example.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

print(res)
