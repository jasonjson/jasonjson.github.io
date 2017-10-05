#!/usr/bin/python

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1

        ret = 0
        for i in xrange(32):
            digit = 0
            for num in nums:
                if (num >> i) & 1:
                    digit += 1
            ret |= (digit % 3) << i
        print digit
        return self.convert(ret)
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
