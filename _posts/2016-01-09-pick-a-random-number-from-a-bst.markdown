---
layout: post
title: Pick a random number from a BST
date: 2016-01-09 10:40:16.000000000 -05:00
categories:
- Brain teaser
author: Jason
---
<p><strong><em>Randomly pick a number fro binary searach tree</em></strong></p>

``` java
public class Solution {
    public static void main(String[] args) {
        TreeNode t1 = new TreeNode(1);
        TreeNode t2 = new TreeNode(2);
        TreeNode t3 = new TreeNode(3);
        TreeNode t4 = new TreeNode(4);
        TreeNode t5 = new TreeNode(5);
        TreeNode t6 = new TreeNode(6);
        t1.left = t2;
        t1.right = t3;
        t2.left = t4;
        t2.right = t5;
        t3.left = t6;
        System.out.println(pickRandom(t1));
        System.out.println(pickRandom(t1));
        System.out.println(pickRandom(t1));
        System.out.println(pickRandom(t1));
        System.out.println(pickRandom(t1));
        System.out.println(pickRandom(t1));
    }

    public static int pickRandom(TreeNode root) {
        if (root == null) return -1;

        List<integer> nums = getList(root);
        int i = 0, result = nums.get(0);
        Random rand = new Random();
        for (; i < nums.size(); i++) {
            int j = rand.nextInt(i + 1);
            if (j == 0) {
                result = nums.get(i);
            }
        }
        return result;
    }

    public static List<integer> getList(TreeNode root) {
        List<integer> result = new ArrayList<>();
        if (root == null) return result;

        List<integer> left = getList(root.left);
        List<integer> right = getList(root.right);
        result.addAll(left);
        result.add(root.val);
        result.addAll(right);
        return result;
    }
}
```
