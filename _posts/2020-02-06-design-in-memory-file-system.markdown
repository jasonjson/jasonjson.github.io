---
layout: post
title: 588 - Design In Memory File System
date: 2020-02-06
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
Design an in-memory file system to simulate the following functions:

* ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

* mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

* addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

* readContentFromFile: Given a file path, return its content in string format.

```python
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}

class FileSystem:

    def __init__(self):
        self.fs = TrieNode()
        self.file_content = defaultdict(str)

    def ls(self, path: str) -> List[str]:
        if path in self.file_content:
            return path.split("/")[-1:]

        curr = self.fs
        for d in path.split("/"):
            if d in curr.children:
                curr = curr.children[d]
            elif d:
                return []
        return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        curr = self.fs
        for d in path.split("/"):
            if d not in curr.children:
                curr.children[d] = TrieNode()
            curr = curr.children[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.file_content[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.file_content[filePath]
```
