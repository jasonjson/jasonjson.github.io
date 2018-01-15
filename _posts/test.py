#!/usr/bin/python
# -*- coding: utf-8 -*-


from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1

        ret = []
        length, number = len(words[0]), len(words)
        seen_map = defaultdict(int)
        for i in xrange(len(s) - length * number + 1):
            if s[i : i + length] in word_map:
                seen_map = defaultdict(int)
                j = 0
                while j < number:
                    new_s = s[i + j * length: i + (j + 1) * length]
                    print new_s
                    if new_s in word_map:
                        seen_map[new_s] += 1
                        if seen_map[new_s] > word_map[new_s]:
                            break
                    else:
                        break
                    j += 1
                if j == number:
                    ret.append(i)
        return ret
if __name__ == "__main__":
    solution = Solution()
    ret =solution.findSubstring("barfoothefoobarman", ["foo","bar"])
    __import__('pprint').pprint(ret)

