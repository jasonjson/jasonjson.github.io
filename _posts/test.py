#!/usr/bin/python

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0
        num_stack = []
        num, sign = 0, "+"
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char != " " and !char.isdigit():
                if sign == "+":
                    num_stack.append(num)
                elif sign == "-":
                    num_stack.append(-num)
                elif sign == "*":
                    num_stack.append(num_stack.pop() * num)
                elif sign == "/":
                    num_stack.append(int(num_stack.pop() / float(num)))
                sign = char
                num = 0

        import pprint
        pprint.pprint(num_stack)
        return sum(num_stack)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.calculate("14-3/2"))
