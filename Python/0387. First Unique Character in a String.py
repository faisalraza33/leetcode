# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# Example 1:
#
# Input: s = "leetcode"
# Output: 0
#
# Example 2:
#
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
#
# Input: s = "aabb"
# Output: -1
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.


# 1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.index(c) == s.rindex(c):
                return i
        return -1


# 2) Hashmap
# Time O(n)
# Space O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i

        return -1
