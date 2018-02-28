class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        if not s:
            return ""

        is_bold = [False] * len(s)
        end = 0
        for i in xrange(len(s)):
            for word in dict:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            is_bold[i] = end > i

        ret, bold_s = [], []
        for i, char in enumerate(s):
            if is_bold[i]:
                bold_s.append(char)
            else:
                ret.append("<b>" + "".join(bold_s) + "</b>")
                ret.append(char)
                bold_s = []
        return "".join(ret)

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.addBoldTag("aaabbcc", ["aaa","aab","bc"]))
