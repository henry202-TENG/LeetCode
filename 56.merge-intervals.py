#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from hashlib import new
from heapq import merge


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        while intervals:
            n = len(intervals)
            for j in range(n):
                if not intervals: continue
                inter = intervals.pop(0)
                for i in range(n-1):
                    if not intervals: continue
                    inter_2ed = intervals.pop(0)

                    if inter_2ed[0] <= inter[1]:
                        inter[0] = min(inter[0], inter_2ed[0])
                        inter[1] = max(inter[1], inter_2ed[1])
                    else:
                        inter_2ed = [inter_2ed]
                        inter_2ed.extend(intervals) # 為了保持順序不變
                        intervals = inter_2ed
                        break
                res.append(inter)
        return res

# @lc code=end

