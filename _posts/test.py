class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return []

        ret = []
        self.helper(word, 0, [], ret, False)
        return ret

    def helper(self, word, start, curr, ret, add_number):
        if start == len(word):
            ret.append("".join(curr))
            return
        if not add_number:
            for i in xrange(start + 1, len(word) + 1):
                number = str(i - start)
                self.helper(word, i, curr + [number], ret, True)
        self.helper(word, start + 1, curr + [word[start]], ret, False)
if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.generateAbbreviations("word"))
