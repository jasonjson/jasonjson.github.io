class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        if not num:
            return []

        ret = []
        self.helper(num, target, [], 0, 0, ret)
        return ret

    def helper(self, num, target, curr, prev, curr_ret, ret):
        if len(num) == 0:
            if target == curr_ret:
                ret.append("".join(curr))
            return
        for i in xrange(1, len(num) + 1):
            new_num = int(num[:i])
            if len(curr) == 0:
                self.helper(num[i:], target, [str(new_num)], new_num, new_num, ret)
            else:
                self.helper(num[i:], target, curr + ["+", str(new_num)], new_num, curr_ret + new_num, ret)
                self.helper(num[i:], target, curr + ["-", str(new_num)], -new_num, curr_ret - new_num, ret)
                self.helper(num[i:], target, curr + ["*", str(new_num)], prev * new_num, curr_ret - prev + prev * new_num, ret);
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.addOperators("123", 6))
