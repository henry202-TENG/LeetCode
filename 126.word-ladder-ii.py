#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def word_diff_one(word1, word2):
        diff_digit = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                diff_digit +=1
            if diff_digit > 1:
                return False
        if diff_digit:
            return True
        else:
            return False

    def BFS(self, word):
        pass

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        
# @lc code=end

