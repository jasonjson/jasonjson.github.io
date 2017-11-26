
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        size = len(self.to_binary(num))
        return num ^ ((1 << size) - 1)


    def to_binary(self, num):
        ret = []
        while num:
            ret.append(str(num % 2))
            num /= 2
        return "".join(ret)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.findComplement(5))
