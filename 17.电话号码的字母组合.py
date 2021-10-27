#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# %%
from typing import List


class Solution:
    def __init__(self) -> None:
        self.klg = ['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        re = list()
        fistr_digit = digits[0]
        sub_res = self.get_sub(digits[1:])
        if fistr_digit != 1:
            for pre in self.klg[int(fistr_digit)-1]:
                for _ in sub_res:
                    re.append(pre+_)
        else:
            #TODO
            return []
        return re
    
    def get_sub(self, substr):
        if not substr:
            return []
        elif len(substr) == 1:
            return self.klg[int(substr)-1]
        else:
            re =[]
            fistr_digit = substr[0]
            sub_res = self.sub(substr[1:])
            if fistr_digit != 1:
                for pre in self.klg[fistr_digit-1]:
                    for _ in sub_res:
                        re.append(pre+_)
            return re
# @lc code=end 

# %%
s = Solution()
digits = "23"
s.letterCombinations(digits=digits)
# %%
