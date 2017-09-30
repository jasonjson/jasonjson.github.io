#!/usr/bin/python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if not rowIndex:
            return []

        ret = [0] * (rowIndex + 1)
        for i in xrange(1, rowIndex + 2):
            # import pdb
            # pdb.set_trace()
            for j in reversed(xrange(i)):
                if j == 0 or j == i - 1:
                    ret[j] = 1
                else:
                    ret[j] = ret[j] + ret[j - 1]
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.getRow(3))


