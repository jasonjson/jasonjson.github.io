---
layout: post
title: 297 - Serialize And Deserialize Binary Tree
date: 2017-11-06
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.**


``` java
class Solution {
    public String serialize(TreeNode root) {
        StringBuilder str = new StringBuilder();
        if (root == null) return str.toString();
        serializeHelper(root, str);
        return str.toString();
    }

    public void serializeHelper(TreeNode root, StringBuilder str) {
        if (root == null) {
            str.append("#.");
        } else {
            str.append(root.val + ".");
            serializeHelper(root.left, str);
            serializeHelper(root.right, str);
        }
    }

    public TreeNode deserialize(String data) {
        if (data == null || data.length() == 0) return null;
        String[] strs = data.split(".");
        int[] index = new int[] {0};
        return deserializeHelper(strs, index);
    }

    public TreeNode deserializeHelper(String[] strs, int[] index) {
        if (index[0] == strs.length) return null;
        String next = strs[index[0]++];
        if (next.equals("#")) {
            return null;
        } else {
            TreeNode root = new TreeNode(Integer.valueOf(next));
            root.left = deserializeHelper(strs, index);
            root.right = deserializeHelper(strs, index);
            return root;
        }
    }
    }
```

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
