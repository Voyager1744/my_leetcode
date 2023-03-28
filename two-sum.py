class Solution:
    def twoSum(self, nums, target):
        res_list = []
        for i in range(len(nums)-1):
            res_list = [i]
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    res_list.append(j)
                    return res_list
        return -1


exemple = Solution()
res = exemple.twoSum([3, 2, 4, 7], 6)

print(res)
