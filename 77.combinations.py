#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution: 
    def combine(self, n: int, k: int) -> List[List[int]]: 
        def dfs(start, cur): 
            # 如果當前已經拿到了K個數的組合，直接加入答案 
            # 注意要做深拷貝，否則在之後的回溯過程當中變動也會影響結果
            if len(cur) == k:
                ret.append(cur[:]) 
                return 
                
            # 從start+1的位置開始遍歷 
            for i in range(start+1, n):
                cur.append(i+1)
                dfs(i, cur)
                # 回溯 
                cur.pop()
                
        ret = []
        dfs(-1, [])
        return ret

# @lc code=end

