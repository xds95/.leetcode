#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):
        docker = []
        if (not nums1) and (not nums2): return 0
        while nums1 or nums2:
            if nums1 and (not nums2):
                docker.append(nums1.pop(0))
            elif nums2 and (not nums1):
                docker.append(nums2.pop(0))
            else:
                if nums1[0]<=nums2[0]: 
                    docker.append(nums1.pop(0))
                else:
                    docker.append(nums2.pop(0))
        if len(docker)%2 == 0:
            return (docker[len(docker)//2-1]+docker[len(docker)//2])/2
        else:
            return docker[len(docker)//2]

# @lc code=end

