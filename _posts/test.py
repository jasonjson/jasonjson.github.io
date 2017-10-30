class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        bulbs = [True] * (n + 1)
        for i in xrange(2, n + 1):
            for j in xrange(1, n + 1):
                if j % i == 0:
                    bulbs[j] = not bulbs[j]
        print bulbs
        return bulbs.count(True) - 1
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.bulbSwitch(3))
