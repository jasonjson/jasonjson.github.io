class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        x, y = 0, 0
        ret = 0
        while x < rows and y < cols:
            x, y = self.helper(sentence, x, y, cols)
            if x < rows:
                ret += 1
        return ret

    def helper(self, words, x, y, cols):
        for word in words:
            if y + len(word) == cols:
                y = 0
                x += 1
            elif y + len(word) + 1 > cols:
                y = len(word) + 1
                x += 1
            else:
                y += len(word) + 1
            print x, y, word
        return x, y

if __name__ == "__main__":
    solution = Solution()
    import pprint
    pprint.pprint(solution.wordsTyping(["a", "bcd", "e"], 5, 6))
