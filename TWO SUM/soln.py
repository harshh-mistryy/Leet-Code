class Solution:
    @staticmethod
    def twoSum(nums: list, target: int):
        for i in nums:
            temp = target - i
            if temp in nums:
                if temp == i:
                    findex = nums.index(i)
                    sindex = nums.index(i, findex + 1)
                    return [findex, sindex]
                return [nums.index(i), nums.index(temp)]

temp = Solution.twoSum(nums=[4,4,4], target=4)
print(temp)

# 0(n2)