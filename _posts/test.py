#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        
        sign, index, ret = 1, 0, 0
        if str[0] == "-":
            sign = -1
            index += 1
        elif str[0] == "+":
            index += 1
        
        has_exp = False
        for char in str[index:]:
            if char not in "0123456789":
                break
            ret = ret * 10 + sign * int(char)
            print int(char)
        if ret >= 2 ** 31:
            return 2 ** 31 - 1
        elif ret < -2 ** 31:
            return -2 ** 31
        return ret

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.myAtoi("123"))
