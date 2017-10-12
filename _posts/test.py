#!/usr/bin/python
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if not n:
            return False
        summation = sum([int(c) ** 2 for c in str(n)])
        print summation
        if summation > 9:
            return self.isHappy(summation)
        else:
            return summation == 1
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.isHappy(1111111))
