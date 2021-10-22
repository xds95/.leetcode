#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
# %%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_length = len(s)
        i,j=0,1
        max_ = 0
        while j<s_length-1:
            s_temp = s[i:j]
            len_s_temp = len(s_temp)
            if len(set(s_temp)) < len_s_temp:
                i+=1
            else:
                j+=1
                max_ = len_s_temp
        return max_
            
# @lc code=end
# %%
if __name__ == '__main__':
    s = "pwwkew"
    so = Solution()
    max_ = so.lengthOfLongestSubstring(s)
    print(max_)
