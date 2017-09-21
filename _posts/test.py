class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if not n:
            return ""

        prev = "1"
        for i in xrange(n - 1):
            count, j = 1, 1
            curr = []
            while j < len(prev):
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    curr.append(str(count))
                    curr.append(prev[j - 1])
                    count = 1
                j += 1
            curr.append(str(count))
            curr.append(prev[j - 1])
            prev = "".join(curr)
            print prev
        return prev

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.countAndSay(6))
