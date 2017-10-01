---
layout: post
title: 103 - Binary Tree Zigzag Level Order Traversal
date: 2015-10-21 02:56:43.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).**


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: A list of lists of integer include
     *          the zigzag level order traversal of its nodes' values
     */
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
        // write your code here
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root == null) return result;

        Queue<treenode> q = new LinkedList<treenode>();
        q.add(root);
        boolean even = true;
        while (!q.isEmpty()) {
            int size = q.size();
            ArrayList<Integer> list = new ArrayList<Integer> ();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            if (even) {
                result.add(list);
            } else {
                Collections.reverse(list);
                result.add(list);
            }
            even = !even;
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        prev = [root]
        ret = []
        reverse = False
        while prev:
            if reverse:
                ret.append([n.val for n in reversed(prev)])
            else:
                ret.append([n.val for n in prev])
            reverse = False if reverse else True
            curr = []
            for node in prev:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            prev = curr
        return ret
```
