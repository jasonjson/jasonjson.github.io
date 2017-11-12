class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        length = 0
        num = 1
        while length < n:
            length += len(str(num))
            if length >= n:
                __import__('pdb').set_trace()
                return int(str(num)[length - n + 1])
            num += 1
        return -1
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findNthDigit(3))
