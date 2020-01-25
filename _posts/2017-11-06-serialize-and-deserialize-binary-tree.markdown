---
layout: post
title: 297 - Serialize And Deserialize Binary Tree
date: 2017-11-06
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.**


```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ret = []
        self.serialize_helper(root, ret)
        return ".".join(ret)

    def serialize_helper(self, root, ret):
        if not root:
            ret.append("#")
        else:
            ret.append(str(root.val))
            self.serialize_helper(root.left, ret)
            self.serialize_helper(root.right, ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        return self.deserialize_helper(data.split("."), [0])

    def deserialize_helper(self, str_list, index):
        if index[0] == len(str_list):
            return
        root_val = str_list[index[0]]
        index[0] += 1
        if root_val == "#":
            return
        else:
            root = TreeNode(int(root_val))
            root.left = self.deserialize_helper(str_list, index)
            root.right = self.deserialize_helper(str_list, index)
            return root
```
