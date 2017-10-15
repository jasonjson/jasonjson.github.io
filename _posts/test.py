#!/usr/bin/python

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.char_map = {}
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if char not in curr.char_map:
                curr.char_map[char] = TrieNode()
            curr = curr.char_map[char]
        curr.is_word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        return self.helper(curr, word)

    def helper(self, root, word):
        for i, char in enumerate(word):
            if char == ".":
                for child in root.char_map.values():
                    if self.helper(child, word[i + 1:]):
                        return True
                return False
            elif char not in root.char_map:
                return False
            root = root.char_map[char]
        return root.is_word
if __name__ == "__main__":
    word = WordDictionary()
    word.addWord("bad")
    import pprint
    # pprint.pprint(word.search("bad"))
    pprint.pprint(word.search("b.."))
