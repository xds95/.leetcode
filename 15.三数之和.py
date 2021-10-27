#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        re=[]
        num_array = [['x' for i in range(len(nums))] for i in range(len(nums))]
        # print(f'num_array:{num_array}')
        for i in range(6):
            for j in range(i+1,6):
                num_array[i][j]= -nums[i]-nums[j] 
        for i in range(6):
            for j in range(i+1,6):
                tmp = nums.copy()
                tmp[:j]=[100 for _ in range(j)]
                try:
                    idx=tmp.index(num_array[i][j])
                    # print(f'[idx]idx:{idx},num_array[{i}][{j}]:{num_array[i][j]},tmp:{tmp}')
                    re.append([nums[i],nums[j],nums[idx]])
                    # print(f'[Append]nums[{i}]:{nums[i]}+nums[{j}]:{nums[j]} +nums{[idx]}:{nums[idx]} == 0')
                except:
                    # print(f'[None]nums[{i}]:{nums[i]}+nums[{j}]:{nums[j]} find not pair in num_array')
                    pass
        [_.sort() for _ in re]
        re1 = re
        # %%
        re2=[]
        for _ in re1:
            if _ not in re2:
                re2.append(_)
        print(re2)
# @lc code=end
