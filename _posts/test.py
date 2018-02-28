class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        stack = [["", 1]]
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append(["", num])
                num = 0
            elif char == "]":
                new_s, count = stack.pop()
                stack[-1][0] += new_s * count
            else:
                stack[-1][0] += char
        new_s, count = stack.pop()
        return new_s * count
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.decodeString("2[abc]3[cd]ef"))
