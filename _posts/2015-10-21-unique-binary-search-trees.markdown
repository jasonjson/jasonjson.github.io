---
layout: post
title: Unique Binary Search Trees
date: 2015-10-21 02:36:32.000000000 -04:00
categories:
- Binary Search Tree
- Dynamic Programming
author: Jason
---
<p><strong><em>Given n, how many structurally unique BST's (binary search trees) that store values 1...n?</em></strong></p>

<a href="http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html">see more explanation here</a></p>

``` java
public class Solution {
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        // write your code here
        if (n < 0) return -1;
        int[] count = new int[n+1]; //count[i] indicates how many BST for i
        count[0] = 1;
        for (int i = 1; i <= n; i++) {//there can be i - 1 elements in the subtree, use j to control how many elements in left subtree and how many in right subtree, update count[i]
            for (int j = 1; j <= i; j++) {
                count[i] += count[j-1] * count[i-j];// (j - 1) + (i - j) == i - 1 elements
            }
        }
        return count[n];
    }
}
```
