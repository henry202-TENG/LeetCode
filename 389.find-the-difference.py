#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # t 多 s 一個字
        # 兩種情況
        # 1. t 比 s 多一種字符，找多出的那一種字符
        # 2. t 跟 s 字符種類一樣，找數量不同的那個字符
        
        def makeHash(s, hash):
            for ss in s:
                if ss not in hash:
                    hash[ss] = 1
                else:
                    hash[ss] += 1
            return hash

        hash_t = makeHash(t, {})
        hash_s = makeHash(s, {})

        # 1. t 比 s 多一種字符，找多出的那一種字符
        for tt in hash_t:
            if tt not in hash_s:
                return tt

        # 2. t 跟 s 字符種類一樣，找數量不同的那個字符
        for tt in hash_t:
            if hash_s[tt] != hash_t[tt]:
                return tt

        
        
# @lc code=end

