#!/usr/bin/python

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        if not input:
            return []

        num_op = self.get_num_op(input)
        print num_op
        return self.helper(num_op, 0, len(num_op) - 1)

    def helper(self, num_op, start, end):
        if start == end:
            return [num_op[start]]
        ret = []
        for i in xrange(start + 1, end, 2):
            operator = num_op[i]
            left_ret = self.helper(num_op, start, i - 1)
            right_ret = self.helper(num_op, i + 1, end)
            for left in left_ret:
                for right in right_ret:
                    if operator == "+":
                        ret.append(left + right)
                    elif operator == "-":
                        ret.append(left - right)
                    elif operator == "*":
                        ret.append(left * right)
        return ret

    def get_num_op(self, input):
        ret = []
        index = 0
        num = 0
        while index < len(input):
            if input[index].isdigit():
                num = num * 10 + int(input[index])
            else:
                ret.append(num)
                ret.append(input[index])
                num = 0
            index += 1
        ret.append(num)
        return ret
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.diffWaysToCompute("2-1-1"))
