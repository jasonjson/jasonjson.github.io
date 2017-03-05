---
layout: post
title: "Verify Preorder Serialization of a Binary Tree"
date: 2016-02-23 21:32:19.000000000 -05:00
tags:
- algorithm
categories:
- Binary Search Tree
---
<p><strong><em>Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.</em></strong></p>


``` java
public class Solution {
//the number of empty is nodes is always one more than the number of numeric nodes in the end
    public static boolean isValidSerialization(String preorder) {
        if (preorder == null || preorder.length() == 0) return false;

        String[] nodes = preorder.split(",");
        int n = 0;
        for (String next : nodes) {
            if (n == 1) return false;//if there are still more nodes and the number of empty nodes
            // is already one more than the numeric node, return false
            n = next.equals("#") ? n + 1 : n - 1;
        }
        return n == 1 ? true : false;//in the end, the number of empty node should be one more than the numeric nodes
    }
}
```
