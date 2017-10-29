class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True
        for i in xrange(1, len(num) / 2 + 1):
            if num[0] == "0" and i > 1:
                break
            # j = 1
            # while max(i , j) <= len(num) - i - j:
            for j in xrange(1, len(num) - i):
                if num[i] == "0" and j > 1:
                    break
                if self.is_valid(int(num[:i]), int(num[i:i+j]), num[i+j:]):
                    return True
                # j += 1
        return False

    def is_valid(self, prev_1, prev_2, num):
        if len(num) == 0:
            return True
        curr = str(prev_1 + prev_2)
        if num.startswith(curr) and self.is_valid(prev_2, int(curr), num[len(curr):]):
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.isAdditiveNumber("123"))
