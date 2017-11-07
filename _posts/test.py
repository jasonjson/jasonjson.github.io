class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """


        return z in self.helper(x, y)

    def helper(self, x, y):
        prev = [x, y]
        added = True
        while added:
            added = False
            for i in xrange(len(prev) - 1):
                for j in xrange(i + 1, len(prev)):
                    num1 = prev[i] + prev[j]
                    if num1 < x and num1 < y and num1 not in prev:
                        prev.append(num1)
                        added = True
                    num2 = abs(prev[i] - prev[j])
                    if num2 not in prev:
                        prev.append(num2)
                        added = True
        print prev
        return prev
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.canMeasureWater(1, 2, 3))
