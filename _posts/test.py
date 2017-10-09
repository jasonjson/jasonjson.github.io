#!/usr/bin/python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if not numerator or not denominator:
            return ""

        ret = []
        nume, deno = abs(numerator), abs(denominator)
        if numerator > 0 == denominator < 0:
            ret.append("-")
        ret.append(str(nume / deno))
        nume %= deno
        if nume == 0:
            return "".join(ret)
        else:
            ret.append(".")
        repeating_map = {}
        index = 1
        while nume:
            print nume
            nume *= 10
            digit = nume / deno
            if nume not in repeating_map:
                ret.append(str(digit))
                repeating_map[nume] = index
                index += 1
            else:
                ret.insert(ret.index(".") + repeating_map[nume], "(")
                ret.append(")")
                break
            nume %= deno
        return "".join(ret)
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.fractionToDecimal(1, 6))
