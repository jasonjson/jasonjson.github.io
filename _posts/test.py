#!/usr/bin/python

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if len(s) == 0:
            return True

        for i in xrange(len(s)):
            if s[: i + 1] in wordDict and self.wordBreak(s[i + 1 :], wordDict):
                return True

        return False
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.wordBreak("leetcode", ["leet", "code"]))
