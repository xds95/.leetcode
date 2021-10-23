#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        debug=False
        len_s = len(s)
        max_xyx_str = ''
        max_xyx_len = 0
        for i in range(len_s):
            for j in range(len_s,0,-1):
                if j-i+1 < max_xyx_len:break
                if debug: print(f'do i:{i}, j:{j},s[i:j]:{s[i:j]}')
                if self.isxyx_2(s[i:j]):
                    if len(s[i:j])>max_xyx_len:
                        if debug: print(f'get xyx, len(s[i:j]):{len(s[i:j])},max_xyx_len:{max_xyx_len}')
                        max_xyx_str = s[i:j]
                        max_xyx_len =len(s[i:j])
                    break
                else:
                    if debug: 
                        print(f's[i:j]:{s[i:j]} is not xyx string')
                    else:
                        pass
        return max_xyx_str
        
    def isxyx_1(self, s):
        i,j=0,len(s)-1
        if len(s)<=1: return True
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    
    def isxyx_2(self,s):
        if s==s[::-1]:
            return True
        else:
            False

# @lc code=end
if __name__ == '__main__':
    s = "babad"
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    so = Solution()
    re = so.longestPalindrome(s)
    print(f're:{re}')
