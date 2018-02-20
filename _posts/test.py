class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            sign = -1
        else:
            sign = 1

        num, den = abs(numerator), abs(denominator)
        ret = []
        ret.append(str(num / den))
        carry = num % den
        if carry == 0:
            return "".join(ret)
        else:
            ret.append(".")
        carry_map = {}
        while carry:
            carry *= 10
            if carry in carry_map:
                ret.insert(carry_map[carry], "(")
                ret.append(")")
                break
            carry_map[carry] = len(ret)
            ret.append(str(carry / den))
            carry = carry % den
        return "".join(ret)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.fractionToDecimal(2, 3))
