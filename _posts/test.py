#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = map(str, range(1, n + 1))
        k -= 1
        factor = 1
        for i in range(1, n):
            factor *= i
        res = []
        for i in reversed(range(n)):
            import pdb
            pdb.set_trace()
            res.append(nums[k / factor])
            nums.remove(nums[k / factor])
            if i != 0:
                k %= factor
                factor /= i
        return "".join(res)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.getPermutation(3, 4))
