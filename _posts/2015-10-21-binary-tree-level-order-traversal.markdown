---
layout: post
title: 102 - Binary Tree Level Order Traversal
date: 2015-10-21 02:50:43.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Binary tree level order traversal.**


``` java
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Level order a list of lists of integer
     */
     public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root){
         ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
         if (root == null) return result;

         Queue<treenode> q = new LinkedList<treenode>();
         q.add(root);
         while (!q.isEmpty()) {
            int size = q.size();
            //control when the level ends
            ArrayList<Integer> list = new ArrayList<Integer>();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                list.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(list);
         }
         return result;
     }
}
```

``` python
class Solution(object):
    def levelOrder(self, root):
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
        return ret
```
