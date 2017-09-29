---
layout: post
title: Binary Tree Level Order Traversal II
date: 2015-10-21 02:51:04.000000000 -04:00
tags:
- Algorithm
categories:
- Binary Search Tree
author: Jason
---
**Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).**


``` java
 public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: buttom-up level order a list of lists of integer
     */
    public ArrayList<ArrayList<integer>> levelOrderBottom(TreeNode root) {
        // write your code here
        ArrayList<ArrayList<integer>> result = new ArrayList<ArrayList<integer>>();
        if (root == null) return result;

        Queue<treenode> q = new LinkedList<treenode>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            ArrayList<integer> list = new ArrayList<integer>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(list);
        }
        Collections.reverse(result);
        return result;
    }
}
```

``` python
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        prev = [root]
        ret = []
        while prev:
            ret.append([n.val for n in prev])
            curr = []
            for node in prev:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            prev = curr
        return list(reversed(ret))
```
