---
layout: post
title: Verify Preorder Sequence in Binary Search Tree
date: 2015-10-31 17:30:44.000000000 -04:00
categories:
- Binary Search Tree
- Brain teaser
author: Jason
---
<p><strong><em>Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree. You may assume each number in the sequence is unique.<br />

Follow up:<br />
Could you do it using only constant space complexity?</em></strong></p>
``` java
//keeping a stack of nodes (just their values) of which we're still in the left subtree. If the next number is smaller than the last stack value, then we're still in the left subtree of all stack nodes, so just push the new one onto the stack. But once the next number is larger than last stack value, we must now be in their right subtrees (or even further, in the right subtree of an ancestor). Also, use the popped values as a lower bound, since being in their right subtree means we must never come across a smaller number anymore.
//In short, to construct the bst with the sequence, for each element, we shall make sure, when smaller elements come, it is okay, but when there is a bigger one come, then all following elements must be bigger.
public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        if (preorder == null || preorder.length == 0) return true;
        Stack<integer> stack = new Stack<integer>();
        int min = Integer.MIN_VALUE;
        for (int n : preorder) {
            if (n < min) {
                return false;
            }
            while (!stack.isEmpty() && n > stack.peek()) {
                min = stack.pop();关键点就是右子树的所有值都大于左子树！一旦traverse到右子树，后面的所有值必须大于前面的值
            }
            stack.push(n);
        }
        return true;
    }
}
```
``` java
public class Solution {
    public static boolean verifyPostOrder(int[] postOrder) {
        int max = Integer.MAX_VALUE;
        Stack<integer> stack = new Stack<integer>();
        for (int i = postOrder.length - 1; i >= 0; i--) {
            if (postOrder[i] > max) {
                return false;
            }
            while (!stack.isEmpty() && postOrder[i] < stack.peek()) {
                max = stack.pop();
            }
            stack.push(postOrder[i]);
        }
        return true;
    }
}
```
