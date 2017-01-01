---
layout: post
title: Pick a random number from a BST
date: 2016-01-09 10:40:16.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1465846717;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:276;}i:1;a:1:{s:2:"id";i:47;}i:2;a:1:{s:2:"id";i:1058;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
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
</integer></integer></integer></integer></integer></pre>
<p>[/expand]</p>
