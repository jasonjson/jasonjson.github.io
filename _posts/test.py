class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        index = [0]
        return self.helper(s, index)

    def helper(self, s, index):
        ret = []
        while (index[0] < len(s) and s[index[0]] != "]"):
            if s[index[0]].isdigit():
                num = 0
                while index[0] < len(s) and s[index[0]].isdigit():
                    num = num * 10 + int(s[index[0]])
                    index[0] += 1
                __import__('pdb').set_trace()
                index[0] += 1
                string = self.helper(s, index)
                index[0] += 1
                ret.extend([string] * num)
            else:
                ret.append(s[index[0]])
                index[0] += 1
        return "".join(ret)
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.decodeString("3[a]2[bc]"))
