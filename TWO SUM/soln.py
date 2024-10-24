class Solution:
    @staticmethod
    def twoSum(nums: list, target: int):
        for i in range(len(nums)):
            temp = target - nums[i]
            temp_dict = {} 
            temp_dict[temp] = i
            if temp in nums and nums.index(temp) != temp_dict[temp]:
                if temp == nums[i]:
                    findex = nums.index(nums[i])
                    sindex = nums.index(nums[i], findex + 1)
                    return [findex, sindex]
                return [nums.index(nums[i]), nums.index(temp)]


temp = Solution.twoSum(nums=[6,6,8,5,3,2,5,6,7,8,8,8,9,9], target=6)
print(temp)

# 0(n2)