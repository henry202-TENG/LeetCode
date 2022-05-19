/*
 * @lc app=leetcode id=28 lang=cpp
 *
 * [28] Implement strStr()
 */

// @lc code=start
class Solution {
public:
    int strStr(string haystack, string needle) {
        bool found = false;
        int n = haystack.size();

        for (int i=0; i<n; i++)
        {
            if (haystack[i] == needle[0]){
                found = checkSubStr(i, haystack, needle);
            }
            if (found) return i;
        }
        return -1;
    }

    bool checkSubStr(int posi, string haystack, string needle)
    {
        for (int i=0; i<needle.size(); i++)
        {
            if (haystack[posi+i] != needle[i]) return false;
        }
        return true;
    }
};
// @lc code=end

