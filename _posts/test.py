#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s:
            return []

        ret = []
        self.helper(step=0, string=s, curr=[], ret=ret)
        return ret

    def helper(self, step, string, curr, ret):
        if step == 4:
            if not string:
                ret.append(".".join(curr))
                return
        for i in xrange(1, 4):
            if i > len(string):
                return
            val = int(string[:i])
            if val <= 255 and str(val) == string[:i]:
                self.helper(step + 1, string[i:], curr + [string[:i]], ret)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.restoreIpAddresses("010010"))
