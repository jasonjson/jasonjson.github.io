---
layout: post
title: Range Sum Query - Mutable
date: 2015-11-18 21:19:53.000000000 -05:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive. The update(i, val) function modifies nums by updating the element at index i to val.**


<p><a href="https://www.youtube.com/watch?v=CWDQJGaN1gY">read more</a></p>

```java
public class NumArray {
    private int[] arrs;
    private int[] BTree;

    public NumArray(int[] nums) {
        this.arrs = new int[nums.length];//wrong: this.arrs = nums;
        this.BTree = new int[nums.length + 1];
        //arrs = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            update(i, nums[i]);//the initial value of arrs[i] is zero, and thus we can update BTree
            arrs[i] = nums[i];//then we assign value to arrs[i],
        }
    }

    public void update(int i, int val) {
        int diff = val - arrs[i];
        arrs[i] = val;
        i++;//the index of Btree is i ++
        while (i < BTree.length) {
            BTree[i] += diff;
            i += i & (-i);//update next value
        }
    }

    public int getSum(int i) {
        i++;
        int sum = 0;
        while (i > 0) {
            sum += BTree[i];
            i -= i & (-i);//add parents
        }
        return sum;
    }

    public int sumRange(int i, int j) {
        return getSum(j) - getSum(i-1);//i - 1 not i
    }
}
```

```java
public class NumArray {
    segmentTreeNode root;
    public NumArray(int[] nums) {
        this.root = build(nums, 0, nums.length - 1);
    }

    void update(int i, int val) {
        updateNode(root, i, val);
    }

    public int sumRange(int i, int j) {
        return query(root, i, j);
    }

    class segmentTreeNode {
        int start, end, sum;
        segmentTreeNode left, right;
        segmentTreeNode(int start, int end, int sum) {
            this.start = start;
            this.end = end;
            this.sum = sum;
            this.left = null;
            this.right = null;
        }
    }
    public segmentTreeNode build(int[] nums, int start, int end) {
        if (start > end) return null;
        if (start == end) return new segmentTreeNode(start, start, nums[start]);
        int mid = (start + end) / 2;
        segmentTreeNode root = new segmentTreeNode(start, end, 0);
        root.left = build(nums, start, mid);
        root.right = build(nums, mid + 1, end);
        root.sum = root.left.sum + root.right.sum;
        return root;
    }

    public void updateNode(segmentTreeNode root, int i, int val) {
        if (root.start == i && root.end == i) {
            root.sum = val;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (i <= mid) {
            updateNode(root.left, i, val);
        } else {
            updateNode(root.right, i, val);
        }
        root.sum = root.left.sum + root.right.sum;
    }
    public int query(segmentTreeNode root, int start, int end) {
        if (root.start == start && root.end == end) {
            return root.sum;
        }
        int mid = (root.start + root.end) / 2;
        if (start > mid) {
            return query(root.right, start, end);
        } else if (end <= mid) {
            return query(root.left, start, end);
        } else {
            return query(root.left, start, mid) + query(root.right, mid + 1, end);
        }
    }
}
```

```python
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0]
        for num in nums:
            sum = self.sums[-1] + num
            self.sums.append(sum)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        for index in range(i + 1, len(self.sums)):
            self.sums[index] += diff

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]
```

```python
class NumArray(object):

    def __init__(self, nums):
        self.root = self.build(0, len(nums) - 1, nums)

    def update(self, i, val):
        self.updateNode(self.root, i, val)

    def sumRange(self, i, j):
        return self.queryNode(self.root, i, j)

    def build(self, start, end, nums):
        if start > end:
            return None
        elif start == end:
            return segement_node(start, end, nums[start])
        else:
            mid = (start + end) // 2
            root = segement_node(start, end, 0)
            root.left = self.build(start, mid, nums)
            root.right = self.build(mid + 1, end, nums)
            root.sum = root.left.sum + root.right.sum
            return root

    def updateNode(self, node, i, val):
        if node.start == i and node.end == i:
            node.sum = val
            return
        mid = (node.start + node.end) // 2
        if i <= mid:
            self.updateNode(node.left, i, val)
        else:
            self.updateNode(node.right, i, val)
        node.sum = node.left.sum + node.right.sum

    def queryNode(self, node, i, j):
        if node.start == i and node.end == j:
            return node.sum
        mid = (node.start + node.end) // 2
        if i > mid:
            return self.queryNode(node.right, i, j)
        elif j <= mid:
            return self.queryNode(node.left, i, j)
        else:
            return self.queryNode(node.left, i, mid) + self.queryNode(node.right, mid + 1, j)

class segement_node(object):
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = None
        self.right = None
```
