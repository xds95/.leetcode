#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# %% 定义
# @lc code=start
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        dict_tmp = {}
        for idx,num_s in enumerate(nums):
            num_m = str(target-num_s)
            if str(num_s) in dict_tmp:
                return [dict_tmp[str(num_s)], idx]
            dict_tmp[str(num_m)]=idx
# @lc code=end
# %% 
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    s = Solution()
    print(s.twoSum(nums,target))
# %%
