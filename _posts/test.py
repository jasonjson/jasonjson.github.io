class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        vowel = [v for v in reversed(s) if v in "aeiou"]
        ret = []

        index = 0
        for i in xrange(len(s)):
            if s[i] in "aeiou":
                ret.append(vowel[index])
                index += 1
            else:
                ret.append(s[i])
        return "".join(ret)
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.reverseVowels("hello"))
