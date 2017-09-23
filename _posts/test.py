#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1 or not num2:
            return ""

        ret = [0] * (len(num1) * len(num2) + 1)

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                mul = int(n1) * int(n2)
                ret[i + j] += mul
                ret[i + j + 1] += ret[i + j] / 10
                ret[i + j] %= 10
        ret = list(reversed(ret))

        index = 0
        while index < len(ret):
            if ret[index] != 0:
                break
            index += 1
        tmp = []
        for i in xrange(index, len(ret)):
            tmp.append(str(ret[i]))
        return "".join(tmp)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.multiply("98", "9"))
