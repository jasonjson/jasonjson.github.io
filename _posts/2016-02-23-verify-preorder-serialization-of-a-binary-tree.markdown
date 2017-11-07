---
layout: post
title: 331 - Verify Preorder Serialization of a Binary Tree
date: 2016-02-23 21:32:19.000000000 -05:00
tags:
- Leetcode
categories:
- Binary Search Tree
---
**Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.**


``` java
public class Solution {
//the number of empty is nodes is always one more than the number of numeric nodes in the end
    public static boolean isValidSerialization(String preorder) {
        if (preorder == null || preorder.length() == 0) return false;

        String[] nodes = preorder.split(",");
        int n = 0;
        for (String next : nodes) {
            if (n == 1) return false;
            //if there are still more nodes and the number of empty nodes is already one more than the numeric node, return false
            n = next.equals("#") ? n + 1 : n - 1;
        }
        return n == 1 ? true : false;
        //in the end, the number of empty node should be one more than the numeric nodes
    }
}
```

``` python
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        if not preorder:
            return False
        none_nodes_count = 0
        for val in preorder.split(","):
            if none_nodes_count == 1:
                return False
            elif val == "#":
                none_nodes_count += 1
            else:
                none_nodes_count -= 1
        return True if none_nodes_count == 1 else False
```
