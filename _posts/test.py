#!/usr/bin/python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if not s:
            return []

        ret = []
        self.helper(s, [], ret)
        return ret

    def helper(self, s, curr, ret):
        if len(s) == 0:
            ret.append(curr[:])
            return
        for i in xrange(len(s)):
            sub_s = s[0: i + 1]
            if self.is_pali(sub_s):
                curr.append(sub_s)
                self.helper(s[i+1:], curr, ret)
                curr.pop()

    def is_pali(self, s):
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.partition("aab"))
