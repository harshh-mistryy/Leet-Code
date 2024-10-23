class Solution:
    @staticmethod
    def twoSum(nums: list, target: int):
        temp_dict = {}
        # breakpoint()
        for i in range(len(nums)) :
            if (target - nums[i]) not in temp_dict:
                temp_dict[nums[i]] = i
            
            elif (target - nums[i]) in temp_dict:
                return [temp_dict[target- nums[i]], i]      

temp = Solution.twoSum(nums=[4,4,3], target=8)
print(temp)