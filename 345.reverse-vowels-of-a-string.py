#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']
        st = []
        sr = ""

        for ss in s:
            if ss in vowels:
                st.append(ss)

        st.reverse()

        for ss in s:
            if ss in vowels:
                sr += st.pop(0)
            else:
                sr += ss

        return sr
        
# @lc code=end

